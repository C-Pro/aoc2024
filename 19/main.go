package main

import (
	"fmt"
	"io"
	"os"
	"strings"

	"github.com/c-pro/geche"
)

/*
Input file example:

r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
*/

func main() {
	f, err := os.Open(os.Args[1])
	if err != nil {
		panic(err)
	}

	avail := geche.NewKV(geche.NewMapCache[string, string]())
	want := []string{}
	total := 0
	total2 := int64(0)

	data, err := io.ReadAll(f)
	if err != nil {
		panic(err)
	}

	for i, line := range strings.Split(string(data), "\n") {
		line = strings.TrimSpace(line)
		if len(line) == 0 {
			continue
		}

		if i == 0 {
			for _, c := range strings.Split(line, ",") {
				c = strings.TrimSpace(c)
				avail.Set(c, c)
			}
			continue
		}

		want = append(want, line)
	}

	for _, w := range want {
		if possible(avail, w) {
			total++
		}
		total2 += countPossible(avail, w)
	}

	fmt.Println("1:", total)
	fmt.Println("2:", total2)
}

func possible(avail *geche.KV[string], want string) bool {
	if _, err := avail.Get(want); err == nil {
		return true
	}

	for l := 1; l < len(want); l++ {
		if _, err := avail.Get(want[:l]); err == nil {
			if possible(avail, want[l:]) {
				return true
			}
		}
	}

	return false
}

var cache = map[string]int64{}

func countPossible(avail *geche.KV[string], want string) int64 {
	if n, ok := cache[want]; ok {
		return n
	}

	n := int64(0)
	if _, err := avail.Get(want); err == nil {
		n++
	}

	for l := 1; l < len(want); l++ {
		if _, err := avail.Get(want[:l]); err == nil {
			n += countPossible(avail, want[l:])
		}
	}

	cache[want] = n

	return n
}
