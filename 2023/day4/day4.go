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
	file, err := os.Open("inputs/day4.txt")
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

func extract(nrs string) map[int]bool {
	n := map[int]bool{}
	for _, num := range strings.Fields(nrs) {
		num = strings.TrimSpace(num)
		nr, err := strconv.Atoi(num)
		if err == nil {
			n[nr] = true
		}
	}
	return n
}

func part1(lines []string) int {
	sum := 0
	for _, line := range lines {
		nrs := strings.Split(line, ":")[1]
		split := strings.Split(nrs, "|")
		win, hand, score := extract(split[0]), extract(split[1]), 0
		for k := range hand {
			if _, ok := win[k]; ok {
				if score == 0 {
					score += 1
				} else {
					score *= 2
				}
			}
		}
		sum += score
	}
	return sum
}

type Game struct {
	id    int
	score int
}

func part2(lines []string) int {
	games := []Game{}
	for _, line := range lines {
		iPart, nrs := strings.Split(line, ":")[0], strings.Split(line, ":")[1]
		id, err := strconv.Atoi(iPart[strings.LastIndex(iPart, " ")+1:])
		if err != nil {
			fmt.Println(err)
			os.Exit(1)
		}
		split := strings.Split(nrs, "|")
		win, hand, score := extract(split[0]), extract(split[1]), 0
		for k := range hand {
			if _, ok := win[k]; ok {
				score += 1
			}
		}
		games = append(games, Game{id, score})
	}
	tot := len(games)
	for i := 0; i < tot; i++ {
		if i == len(games) {
			break
		}
		g := games[i]
		//fmt.Printf("(%d) Game %d with score %d. (%d) games: %+v\n", i, g.id, g.score, tot, games)
		//bf := len(games)
		for j := g.id; j < g.id+g.score; j++ {
			games = append(games, games[j])
			tot += 1
		}
		//fmt.Printf("(%d) Game %d with score %d. games: %d -> %d\n", i, g.id, g.score, bf, len(games))
	}
	// for i, game := range games {
	// 	fmt.Printf("Doing %d Game %d with score %d. games: %+v\n", i, game.id, game.score, games)
	// 	for j := game.id; j <= game.id+game.score; j++ {
	// 		games = append(games, games[j])
	// 	}
	// }
	return len(games)
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
