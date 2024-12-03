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

type Game struct {
	time     int
	distance int
}

func getGames(lines []string) []Game {
	times := strings.Fields(lines[0])[1:]
	dsts := strings.Fields(lines[1])[1:]
	games := []Game{}
	for i := 0; i < len(times); i++ {
		games = append(games, Game{sToI(times[i]), sToI(dsts[i])})
	}
	return games
}

func getGame(lines []string) Game {
	time := strings.Join(strings.Fields(lines[0])[1:], "")
	dst := strings.Join(strings.Fields(lines[1])[1:], "")
	return Game{sToI(time), sToI(dst)}
}

func part1(lines []string) int {
	games := getGames(lines)
	tot := 1
	for _, g := range games {
		wins := 0
		for i := 0; i < g.time; i++ {
			if (g.time-i)*i > g.distance {
				wins += 1
			}
		}
		tot *= wins
	}
	return tot
}

func part2(lines []string) int {
	g := getGame(lines)
	fmt.Println(g)
	tot := 0
	for i := 0; i < g.time; i++ {
		if (g.time-i)*i > g.distance {
			tot += 1
		}
	}
	return tot
}

func main() {
	fmt.Println("Trying in GO !")

	start := time.Now()
	lines := readInputLines("inputs/day6.txt")
	p1 := part1(lines)
	p2 := part2(lines)
	end := time.Since(start).Seconds()

	fmt.Printf("Part 1: %d\n", p1)
	fmt.Printf("Part 2: %d\n", p2)
	fmt.Printf("%fs\n", end)
}
