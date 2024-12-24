package main

import (
	"fmt"
	"io"
	"os"
	"slices"
	"sort"
	"strings"
)

func main() {
	fname := "test.txt"
	if len(os.Args) > 1 {
		fname = os.Args[1]
	}
	f, err := os.Open(fname)
	if err != nil {
		panic(err)
	}

	g := map[string][]string{}
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
			n = []string{}
		}
		n = append(n, parts[1])
		g[parts[0]] = n

		n, ok = g[parts[1]]
		if !ok {
			n = []string{}
		}
		n = append(n, parts[0])
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
		mpp := getMaxFC(g, s, s, []string{s})
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
	fmt.Println("2:", strings.Join(mp, ","))
}

func getSizeNLoops(g map[string][]string, start, curr string, path []string, maxDepth int) []string {
	if maxDepth == 0 {
		return []string{}
	}

	res := []string{}
	for _, next := range g[curr] {
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

func getMaxFC(g map[string][]string, start, curr string, path []string) []string {
	mp := path
	for _, next := range g[curr] {
		if slices.Contains(path, next) {
			continue
		}
		fc := true
		for _, p := range path {
			if !slices.Contains(g[next], p) {
				fc = false
				break
			}
		}
		if fc {
			mpp := getMaxFC(g, start, next, append(path, next))
			if len(mpp) > len(mp) {
				mp = mpp
			}
		}
	}

	return mp
}
