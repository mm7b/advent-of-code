package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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

var CARD_STRENGHT = map[rune]int{
	'A': 14,
	'K': 13,
	'Q': 12,
	'J': 11,
	'T': 10,
}

type Hand struct {
	cards string
	bet   int
	rank  int
}

func getRank(cards string) int {
	m := map[rune]int{}
	for _, r := range cards {
		n, ok := m[r]
		if ok {
			m[r] = n + 1
		} else {
			m[r] = 1
		}
	}

	switch l := len(m); l {
	case 1:
		return 6
	case 2:
		if n, _ := m[[]rune(cards)[0]]; n == 2 || n == 3 {
			return 4
		} else {
			return 6
		}
	case 3:
		for _, v := range m {
			if v == 3 {
				return 3
			}
		}
		return 2
	case 4:
		return 1
	default:
		return 0
	}
}

func getHands(lines []string) []Hand {
	hands := []Hand{}
	for _, line := range lines {
		split := strings.Fields(line)
		hands = append(hands, Hand{split[0], sToI(split[1]), getRank(split[0])})
	}
	return hands
}

func part1(lines []string) int {
	hands := getHands(lines)
	// fmt.Println("Before sort", hands)
	sort.Slice(hands, func(i, j int) bool {
		if hands[i].rank == hands[j].rank {
			for k := 0; k < 5; k++ {
				// fmt.Println("In comparison :", hands[i].cards, hands[j].cards, hands[i].cards[k], hands[j].cards[k], hands[i].cards[k] != hands[j].cards[k])
				if hands[i].cards[k] != hands[j].cards[k] {
					nri, oki := strconv.Atoi(string([]rune(hands[i].cards)[k]))
					nrj, okj := strconv.Atoi(string([]rune(hands[j].cards)[k]))
					if oki == nil {
						if okj != nil || nri < nrj {
							return true
						}
						return false
					} else {
						// fmt.Println("Card strength", []rune(hands[i].cards)[k], []rune(hands[j].cards)[k], CARD_STRENGHT[[]rune(hands[i].cards)[k]] > CARD_STRENGHT[[]rune(hands[j].cards)[k]])
						if okj == nil || CARD_STRENGHT[[]rune(hands[i].cards)[k]] > CARD_STRENGHT[[]rune(hands[j].cards)[k]] {
							return false
						}
						return true
					}
				}
			}
		}
		return hands[i].rank < hands[j].rank
	})
	// fmt.Println("After sort", hands)
	tot := 0
	for i, h := range hands {
		tot += (i + 1) * h.bet
	}
	fmt.Println(len(hands))
	return tot
}

func part2(lines []string) int {
	return 0
}

func main() {
	fmt.Println("Trying in GO !")

	start := time.Now()
	lines := readInputLines("inputs/day7.txt")
	p1 := part1(lines)
	p2 := part2(lines)
	end := time.Since(start).Seconds()

	fmt.Printf("Part 1: %d\n", p1)
	fmt.Printf("Part 2: %d\n", p2)
	fmt.Printf("%fs\n", end)
}
