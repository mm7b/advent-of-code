package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
	"unicode"
)

func splitLine(s, sep string) (string, string) {
	x := strings.Split(s, sep)
	return x[0], x[1]
}

func readInputLines(filePath string) []string {
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Opening file error", err)
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func sToI(s string) int {
	nr, err := strconv.Atoi(s)
	if err == nil {
		return nr
	}
	panic(err)
}

func getSeeds(line string) []int {
	split := strings.Fields(line)
	seeds := []int{}
	for i, s := range split {
		if i == 0 {
			continue
		}
		s = strings.TrimSpace(s)
		seeds = append(seeds, sToI(s))
	}
	return seeds
}

func getSeedRange(line string) []int {
	split := strings.Fields(line)
	seeds := []int{}
	for i := 1; i < len(split); i += 2 {
		s, s1 := sToI(strings.TrimSpace(split[i])), sToI(strings.TrimSpace(split[i+1]))
		end := s + s1
		for s < end {
			seeds = append(seeds, s)
			s += 1
		}
	}
	return seeds
}

type convertMap struct {
	source int
	dest   int
	length int
}

func getMap(l string) convertMap {
	if l == "" {
		return convertMap{}
	}
	split := strings.Fields(l)
	dest, source, length := sToI(split[0]), sToI(split[1]), sToI(split[2])
	return convertMap{source, dest, length}
}

func getMin(seeds []int, lines []string) int {
	min := -1
	maps := [][]convertMap{}
	currentMap := []convertMap{}
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		if c := []rune(line)[0]; unicode.IsLetter(c) {
			if len(currentMap) > 0 {
				maps = append(maps, currentMap)
				currentMap = nil
			}
		} else {
			m := getMap(line)
			if m != (convertMap{}) {
				currentMap = append(currentMap, m)
			}
		}
	}
	if len(currentMap) > 0 {
		maps = append(maps, currentMap)
		currentMap = nil
	}

	for _, s := range seeds {
		val := s
		for _, convertMap := range maps {
			for _, m := range convertMap {
				if m.source <= val && val < m.source+m.length {
					val = m.dest + (val - m.source)
					break
				}
			}
		}
		if min == -1 || val < min {
			min = val
		}
	}
	return min
}

func part1(lines []string) int {
	seeds := getSeeds(lines[0])
	fmt.Println("Nr of seeds part 1: ", len(seeds))
	return getMin(seeds, lines[1:])
}

func part2(lines []string) int {
	seeds := getSeedRange(lines[0])
	fmt.Println("Nr of seeds part 2: ", len(seeds))
	return getMin(seeds, lines[1:])
}

func main() {
	fmt.Println("Trying in GO !")

	start := time.Now()
	lines := readInputLines("inputs/day5.txt")
	p1 := part1(lines)
	p2 := part2(lines)
	end := time.Since(start).Seconds()

	fmt.Printf("Part 1: %d\n", p1)
	fmt.Printf("Part 2: %d\n", p2)
	fmt.Printf("%fs\n", end)
}
