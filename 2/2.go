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

	var keyboard [5][]string
	keyboard[0] = []string{"-", "-", "1", "-", "-"}
	keyboard[1] = []string{"-", "2", "3", "4", "-"}
	keyboard[2] = []string{"5", "6", "7", "8", "9"}
	keyboard[3] = []string{"-", "A", "B", "C", "-"}
	keyboard[4] = []string{"-", "-", "D", "-", "-"}

	pos := [2]int{0, 2}

	for _, line := range lines {
		for _, char := range line {
			dir := fmt.Sprintf("%c", char)

			if dir == "U" {
				if pos[0] != 0 && keyboard[pos[0]-1][pos[1]] != "-" {
					pos[0] -= 1
				}
			} else if dir == "R" {
				if pos[1] != 4 && keyboard[pos[0]][pos[1]+1] != "-" {
					pos[1] += 1
				}
			} else if dir == "D" {
				if pos[0] != 4 && keyboard[pos[0]+1][pos[1]] != "-" {
					pos[0] += 1
				}
			} else if dir == "L" {
				if pos[1] != 0 && keyboard[pos[0]][pos[1]-1] != "-" {
					pos[1] -= 1
				}
			}
		}

		fmt.Println(keyboard[pos[0]][pos[1]])
	}
}
