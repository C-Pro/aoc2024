package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	f, err := os.Open(os.Args[1])
	if err != nil {
		panic(err)
	}

	avail := map[string]struct{}{}
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
				avail[c] = struct{}{}
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

func possible(avail map[string]struct{}, want string) bool {
	if _, ok := avail[want]; ok {
		return true
	}

	for l := 1; l < len(want); l++ {
		if _, ok := avail[want[:l]]; ok {
			if possible(avail, want[l:]) {
				return true
			}
		}
	}

	return false
}

var cache = map[string]int64{}

func countPossible(avail map[string]struct{}, want string) int64 {
	if n, ok := cache[want]; ok {
		return n
	}

	n := int64(0)
	if _, ok := avail[want]; ok {
		n++
	}

	for l := 1; l < len(want); l++ {
		if _, ok := avail[want[:l]]; ok {
			n += countPossible(avail, want[l:])
		}
	}

	cache[want] = n

	return n
}
