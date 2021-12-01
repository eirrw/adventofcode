package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	if len(os.Args) == 2 {
		day, err := strconv.Atoi(os.Args[1])
		if err != nil {
			log.Fatal(err)
		}

		switch day {
		case 1:
			err = day1()
		}
		if err != nil {
			log.Fatal(err)
		}
	} else {
		log.Fatal("Day number required")
	}
}

func getInput(day int) ([]byte, error) {
	input, err := os.ReadFile(fmt.Sprintf("input/%d.input", day))
	if err != nil {
		return nil, err
	}

	return input, nil
}

func getInputAsStrings(day int) ([]string, error) {
	input, err := getInput(day)
	if err != nil {
		return nil, err
	}

	inputStrings := strings.Split(string(input), "\n")

	return inputStrings, nil
}

func getInputAsInts(day int) ([]int, error) {
	inputStrings, err := getInputAsStrings(day)
	if err != nil {
		return nil, err
	}

	inputInts, err := arrayAtoi(inputStrings)
	if err != nil {
		return nil, err
	}

	return inputInts, nil
}

func arrayAtoi(strings []string) ([]int, error) {
	ints := make([]int, len(strings))
	for i, s := range strings {
		if len(s) == 0 {
			continue
		}
		c, err := strconv.Atoi(s)
		if err != nil {
			return nil, err
		}

		ints[i] = c
	}

	return ints, nil
}
