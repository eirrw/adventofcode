package main

import (
	"fmt"
	"strings"
)

func day1() error {
	input, err := getInput(1)
	if err != nil {
		return err
	}

	inputLines, err := arrayAtoi(strings.Split(string(input), "\n"))
	if err != nil {
		return err
	}

	var prev int
	totDec := 0
	for i, line := range inputLines {
		if i != 0 {
			if line > prev{
				totDec++
			}
		}
		
		prev = line
	}
	
	fmt.Printf("pt1: %d\n", totDec)

	totDec = 0
	for i := 0; i < len(inputLines) - 2; i++ {
		cur := inputLines[i] + inputLines[i + 1] + inputLines[i + 2]
		if i != 0 {
			if cur > prev {
				totDec++
			}
		}

		prev = cur
	}

	fmt.Printf("pt2: %d\n", totDec)

	return nil
}
