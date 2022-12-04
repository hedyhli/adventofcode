package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strings"
)

var ascii = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

func getCode(ch rune) int {
	return strings.IndexRune(ascii, ch) + 1
}

func fillSet(chars []rune) (set map[rune]struct{}) {
	var a struct{}
	set = make(map[rune]struct{})
	for _, char := range chars {
		set[char] = a
	}
	return
}

func part1(lines []string) (priorities int) {
	var half int
	var left, right map[rune]struct{}
	for _, line := range lines {
		half = len(line) / 2
		left = fillSet([]rune(line)[half:])
		right = fillSet([]rune(line)[:half])
		// Find intersection
		for char := range left {
			if _, ok := right[char]; ok {
				priorities += getCode(char)
			}
		}
	}
	return
}

func part2(lines []string) (priorities int) {
	var set1, set2, set3 map[rune]struct{}
	for i := 0; i < len(lines); i += 3 {
		set1 = fillSet([]rune(lines[i]))
		set2 = fillSet([]rune(lines[i+1]))
		set3 = fillSet([]rune(lines[i+2]))
		// Find intersections
		for char := range set1 {
			_, ok1 := set2[char]
			_, ok2 := set3[char]
			if ok1 && ok2 {
				priorities += getCode(char)
			}
		}
	}
	return
}

func main() {
	f, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	lines := strings.Split(strings.Trim(string(f), "\n"), "\n")
	fmt.Println(part1(lines))
	fmt.Println(part2(lines))
}
