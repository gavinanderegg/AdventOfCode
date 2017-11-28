package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	dat, err := ioutil.ReadFile("input")
	check(err)

	directions := strings.Split(string(dat), ", ")
	compass := []string{"N", "E", "S", "W"}
	heading := 0

	xDist := 0
	yDist := 0

	for _, direction := range directions {
		r := regexp.MustCompile(`([L|R])(\d+)`)

		turn := r.FindStringSubmatch(direction)[1]
		dist, err := strconv.Atoi(r.FindStringSubmatch(direction)[2])
		check(err)

		if turn == "L" {
			if heading == 0 {
				heading = 3
			} else {
				heading -= 1
			}
		} else {
			if heading == 3 {
				heading = 0
			} else {
				heading += 1
			}
		}

		if compass[heading] == "N" {
			yDist += dist
		} else if compass[heading] == "E" {
			xDist += dist
		} else if compass[heading] == "S" {
			yDist -= dist
		} else if compass[heading] == "W" {
			xDist -= dist
		}
	}

	if xDist < 0 {
		xDist = -xDist
	}

	if yDist < 0 {
		yDist = -yDist
	}

	totalDistance := xDist + yDist

	fmt.Println(totalDistance)
}
