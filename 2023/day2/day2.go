package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func splitLine(s, sep string) (string, string) {
	x := strings.Split(s, sep)
	return x[0], x[1]
}

func readInputLines() []string {
	file, err := os.Open("inputs/day2.txt")
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

func part1(lines []string) int {
	bag := map[string]int{"red": 12, "green": 13, "blue": 14}

	var acceptedIds []int
	for _, line := range lines {
		idPart, seqPart := splitLine(line, ":")
		id, _ := strconv.Atoi(strings.Fields(idPart)[1])
		add := true
		for _, seq := range strings.Split(seqPart, ";") {
			for _, info := range strings.Split(seq, ",") {
				split := strings.Fields(info)
				nr, c := split[0], split[1]
				if n, _ := strconv.Atoi(nr); n > bag[c] {
					add = false
					break
				}
			}
			if !add {
				break
			}
		}

		if add {
			acceptedIds = append(acceptedIds, id)
		}
	}

	sum := 0
	for _, val := range acceptedIds {
		sum += val
	}
	return sum
}

func part2(lines []string) int {
	powers := 0

	for _, line := range lines {
		seqPart := strings.Split(line, ":")[1]
		minBag := map[string]int{"red": 0, "green": 0, "blue": 0}
		for _, seq := range strings.Split(seqPart, ";") {
			for _, cube := range strings.Split(seq, ",") {
				split := strings.Fields(cube)
				if nr, _ := strconv.Atoi(split[0]); minBag[split[1]] < nr {
					minBag[split[1]] = nr
				}
			}
		}
		mul := 1
		for _, v := range minBag {
			mul *= v
		}
		powers += mul
	}

	return powers
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
