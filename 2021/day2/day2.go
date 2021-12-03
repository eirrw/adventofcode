package day2

import (
	"aoc2021/util"
	"fmt"
	"strconv"
)

const cmdUp = "up"
const cmdDn = "down"
const cmdFd = "forward"

func Run() error {
	p1, err := part1()
	if err != nil {
		return err
	}

	p2, err := part2()
	if err != nil {
		return err
	}

	fmt.Printf("part1: %d\npart2: %d\n", p1, p2)

	return nil
}

func part1() (int, error) {
	input, err := util.GetInputMultiDimensionalString(2)
	if err != nil {
		return 0, err
	}

	x, y := 0, 0

	for _, strings := range input {
		v, err := strconv.Atoi(strings[1])
		if err != nil {
			return 0, err
		}

		switch strings[0] {
		case cmdFd:
			x += v
		case cmdDn:
			y += v
		case cmdUp:
			y -= v
		}
	}

	return x*y, nil
}

func part2() (int, error) {
	input, err := util.GetInputMultiDimensionalString(2)
	if err != nil {
		return 0, err
	}

	x, y, a := 0, 0, 0

	for _, strings := range input {
		v, err := strconv.Atoi(strings[1])
		if err != nil {
			return 0, err
		}

		switch strings[0] {
		case cmdFd:
			x += v
			y += v*a
		case cmdDn:
			a += v
		case cmdUp:
			a -= v
		}
	}

	return x*y, nil
}
