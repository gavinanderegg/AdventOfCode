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

	route := make([]string, 0)

	foundDup := false

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

		for i := 0; i < dist; i++ {
			if compass[heading] == "N" {
				yDist += 1
			} else if compass[heading] == "E" {
				xDist += 1
			} else if compass[heading] == "S" {
				yDist -= 1
			} else if compass[heading] == "W" {
				xDist -= 1
			}

			position := strconv.Itoa(xDist) + ", " + strconv.Itoa(yDist)

			for _, stop := range route {
				if stop == position {
					if xDist < 0 {
						xDist = -xDist
					}

					if yDist < 0 {
						yDist = -yDist
					}

					totalDistance := xDist + yDist

					if !foundDup {
						fmt.Println("Duplicate found: " + strconv.Itoa(totalDistance))
						foundDup = true
					}
				}
			}

			route = append(route, position)
		}
	}
}
