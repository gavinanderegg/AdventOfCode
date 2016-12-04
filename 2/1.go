package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	file, err := os.Open("input")
	check(err)
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	var keyboard [3][]int
	keyboard[0] = []int{1, 2, 3}
	keyboard[1] = []int{4, 5, 6}
	keyboard[2] = []int{7, 8, 9}

	pos := [2]int{1, 1}

	for _, line := range lines {
		for _, char := range line {
			dir := fmt.Sprintf("%c", char)

			if dir == "U" {
				if pos[0] != 0 {
					pos[0] -= 1
				}
			} else if dir == "R" {
				if pos[1] != 2 {
					pos[1] += 1
				}
			} else if dir == "D" {
				if pos[0] != 2 {
					pos[0] += 1
				}
			} else if dir == "L" {
				if pos[1] != 0 {
					pos[1] -= 1
				}
			}
		}

		fmt.Println(keyboard[pos[0]][pos[1]])
	}
}
