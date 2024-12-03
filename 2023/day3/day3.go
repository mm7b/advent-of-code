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

func readInputLines() []string {
	file, err := os.Open("inputs/day3.txt")
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

func getDir(dir string) (dx, dy int) {
	switch dir {
	case "left":
		return 0, -1
	case "right":
		return 0, 1
	case "up":
		return -1, 0
	case "down":
		return 1, 0
	case "uLeft":
		return -1, -1
	case "uRight":
		return -1, 1
	case "dLeft":
		return 1, -1
	case "dRight":
		return 1, 1
	}
	return 0, 0
}

func handleMatch(lines []string, i, j int, dir string) (Pair, int) {
	dx, dy := getDir(dir)
	newI, newJ := i+dx, j+dy
	if newI >= 0 && newI < len(lines) {
		if newJ >= 0 && newJ < len(lines[newI]) {
			nj, nr := parseNumber(lines[newI], newJ)
			if nr != -1 {
				return Pair{newI, nj}, nr
			}
			return Pair{-1, -1}, -1
		}
	}
	return Pair{-1, -1}, -1
}

func parseNumber(line string, j int) (int, int) {
	var sb strings.Builder
	for j > 0 && unicode.IsDigit([]rune(line)[j-1]) && unicode.IsDigit([]rune(line)[j]) {
		j -= 1
	}
	for j < len(line) && unicode.IsDigit([]rune(line)[j]) {
		sb.WriteRune([]rune(line)[j])
		j += 1
	}
	n, err := strconv.Atoi(sb.String())
	if err != nil {
		return -1, -1
	}
	return j, n
}

type Pair struct {
	i int
	j int
}

func part1(lines []string) int {
	sum := 0
	directions := [8]string{"left", "right", "up", "down", "uLeft", "uRight", "dLeft", "dRight"}
	visited := map[Pair]bool{}
	for i, line := range lines {
		for j, r := range line {
			if !(unicode.IsDigit(r) || r == '.') {
				for _, dir := range directions {
					if p, nr := handleMatch(lines, i, j, dir); nr != -1 {
						if _, ok := visited[p]; !ok {
							sum += nr
							visited[p] = true
						}
					}
				}
			}
		}
	}
	return sum
}

func part2(lines []string) int {
	sum := 0
	directions := [8]string{"left", "right", "up", "down", "uLeft", "uRight", "dLeft", "dRight"}
	for i, line := range lines {
		for j, r := range line {
			if !(unicode.IsDigit(r) || r == '.') {
				matches := 0
				mul := 1
				visited := map[Pair]bool{}
				for _, dir := range directions {
					if p, nr := handleMatch(lines, i, j, dir); nr != -1 {
						if _, ok := visited[p]; !ok {
							mul *= nr
							matches += 1
							visited[p] = true
						}
					}
				}
				if matches == 2 {
					sum += mul
				}
			}
		}
	}
	return sum
}

func main() {
	fmt.Println("Trying in GO !")

	start := time.Now()
	lines := readInputLines()
	p1 := part1(lines)
	p2 := part2(lines)
	end := time.Since(start).Seconds()

	fmt.Printf("Part 1: %d\n", p1)
	fmt.Printf("Part 2: %d\n", p2)
	fmt.Printf("%fs\n", end)
}
