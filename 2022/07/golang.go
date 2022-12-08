package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var path []string
var dirs map[string]int

var (
	reCd       = regexp.MustCompile(`^\$ cd (.+)`)
	reFileSize = regexp.MustCompile(`(\d+) `)
)

func parseLine(line string) {
	var matchSlice []string
	var d string
	var size int
	var err error

	if strings.HasSuffix(line, "..") {
		path = path[:len(path)-1]
		return
	}

	matchSlice = reCd.FindStringSubmatch(line)
	if len(matchSlice) > 1 {
		d = matchSlice[1]
		path = append(path, d)
		return
	}

	matchSlice = reFileSize.FindStringSubmatch(line)
	if len(matchSlice) > 1 {
		size, err = strconv.Atoi(matchSlice[1])
		if err != nil {
			log.Fatalln("Could not convert", matchSlice[1], "to int")
		}
		// Update all parent directories
		var key string
		for i := 1; i <= len(path); i++ {
			key = strings.Join(path[:i], "/")
			if _, ok := dirs[key]; !ok {
				dirs[key] = 0
			}
			dirs[key] += size
		}
	}
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalln(err)
	}
	defer file.Close()
	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	var line string
	dirs = make(map[string]int)

	// BEGIN main parsing
	for fileScanner.Scan() {
		line = fileScanner.Text()
		parseLine(line)
	}
	// END main parsing

	var (
		// part 1
		sum int

		// part 2
		// minSizeDel set to max first, used to compare and find min later
		minSizeDel int = 7e7
	)

	shouldFree := 3e7 - 7e7 + dirs["/"]

	for _, size := range dirs {
		if size <= 1e5 {
			sum += size
		}
		if size >= shouldFree && size < minSizeDel {
			minSizeDel = size
		}
	}

	fmt.Println("Part 1: Total size of directories under 100,000")
	fmt.Println(sum)
	fmt.Println("Part 2: Smallest directory to delete to have 30,000,000 free")
	fmt.Println(minSizeDel)
}
