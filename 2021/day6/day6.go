package day6

import (
	"aoc2021/util"
	"fmt"
	"strings"
)

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
	inputStr, err := util.GetInputAsStrings(6, false)
	if err != nil {
		return 0, err
	}

	input, err := util.SliceAtoi(strings.Split(inputStr[0], ","))
	if err != nil {
		return 0, err
	}

	fish := calcFish(80, input)

	return fish, nil
}

func part2() (int, error) {
	inputStr, err := util.GetInputAsStrings(6, false)
	if err != nil {
		return 0, err
	}

	input, err := util.SliceAtoi(strings.Split(inputStr[0], ","))
	if err != nil {
		return 0, err
	}

	fish := calcFish(256, input)

	return fish, nil
}

func calcFish(days int, start []int) int {
	fishTracker := make(map[int]int)
	for _, age := range start {
		fishTracker[age]++
	}

	for i := 0; i < days; i++ {
		birthing := fishTracker[0]
		for j := 1; j<= 8; j++ {
			fishTracker[j-1] = fishTracker[j]
		}

		fishTracker[6] += birthing
		fishTracker[8] = birthing
	}

	var totFish int
	for _, i := range fishTracker {
		totFish += i
	}

	return totFish
}
