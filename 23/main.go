package main

import (
	"fmt"
	"io"
	"os"
	"slices"
	"sort"
	"strings"

	"github.com/c-pro/geche"
)

func main() {
	fname := "input.txt"
	if len(os.Args) > 1 {
		fname = os.Args[1]
	}
	f, err := os.Open(fname)
	if err != nil {
		panic(err)
	}

	g := map[string]map[string]struct{}{}
	vertices := map[string]struct{}{}

	data, err := io.ReadAll(f)
	if err != nil {
		panic(err)
	}

	for _, line := range strings.Split(string(data), "\n") {
		line = strings.TrimSpace(line)
		if len(line) == 0 {
			continue
		}

		parts := strings.Split(line, "-")
		n, ok := g[parts[0]]
		if !ok {
			n = map[string]struct{}{}
		}
		n[parts[1]] = struct{}{}
		g[parts[0]] = n

		n, ok = g[parts[1]]
		if !ok {
			n = map[string]struct{}{}
		}
		n[parts[0]] = struct{}{}
		g[parts[1]] = n

		vertices[parts[0]] = struct{}{}
		vertices[parts[1]] = struct{}{}
	}

	lans := map[string]struct{}{}

	mp := []string{}
	for s := range vertices {
		for _, l := range getSizeNLoops(g, s, s, []string{s}, 3) {
			lans[l] = struct{}{}
		}
		mpp := getMaxFC(g, s)
		if len(mpp) > len(mp) {
			mp = mpp
		}
	}

	total := 0
	for l := range lans {
		hasT := false
		for _, v := range strings.Split(l, ",") {
			if strings.HasPrefix(v, "t") {
				hasT = true
				break
			}
		}
		if hasT {
			total++
		}
	}

	fmt.Println("1:", total)
	sort.Strings(mp)
	fmt.Println("2:", strings.Join(mp, ","), len(strings.Join(mp, ",")))
}

func getSizeNLoops(g map[string]map[string]struct{}, start, curr string, path []string, maxDepth int) []string {
	if maxDepth == 0 {
		return []string{}
	}

	res := []string{}
	for next := range g[curr] {
		if maxDepth == 1 && next == start {
			sort.Strings(path)
			return append(res, strings.Join(path, ","))
		}

		if slices.Contains(path, next) {
			continue
		}

		res = append(res, getSizeNLoops(g, start, next, append(path, next), maxDepth-1)...)
	}

	return res
}

func pathKey(path []string) string {
	sort.Strings(path)
	return strings.Join(path, "")
}

var cache = geche.NewRingBuffer[string, struct{}](1000000)

func getMaxFC(g map[string]map[string]struct{}, start string) []string {
	stack := [][]string{{start}}
	mp := stack[0]
	for {
		if len(stack) == 0 {
			break
		}

		if len(stack) > 3 {
			fmt.Println("here")
		}

		path := stack[len(stack)-1]
		curr := path[len(path)-1]
		stack = stack[:len(stack)-1]

		pm := make(map[string]struct{}, len(path))
		for _, p := range path {
			pm[p] = struct{}{}
		}

		for next := range g[curr] {
			if _, ok := pm[next]; ok {
				continue
			}

			np := append(path, next)
			pk := pathKey(np)
			if _, err := cache.Get(pk); err == nil {
				continue
			}

			fc := true
			for _, p := range path {
				if _, ok := g[next][p]; !ok {
					fc = false
					cache.Set(pk, struct{}{})
					break
				}
			}

			if fc {
				if len(np) > len(mp) {
					mp = np
				}

				stack = append(stack, np)
			}
		}
	}

	return mp
}
