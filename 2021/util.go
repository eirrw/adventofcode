package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

// getInput retrieves the input data for the given day from the downloaded input files.
// The data is returned as a byte slice and any read error encountered.
func getInput(day int) ([]byte, error) {
	input, err := os.ReadFile(fmt.Sprintf("input/%d.input", day))
	if err != nil {
		return nil, err
	}

	return input, nil
}

// getInputAsStrings retrieves the input data for the given day from the downloaded input files.
// The data is returned as a slice of strings divided by line and any read error encountered.
func getInputAsStrings(day int) ([]string, error) {
	input, err := getInput(day)
	if err != nil {
		return nil, err
	}

	inputStrings := strings.Split(strings.Trim(string(input), "\n \t"), "\n")

	return inputStrings, nil
}

// getInput retrieves the input data for the given day from the downloaded input files.
// The data is returned as a slice of integers (given one number per line) and any read error encountered.
func getInputAsInts(day int) ([]int, error) {
	inputStrings, err := getInputAsStrings(day)
	if err != nil {
		return nil, err
	}

	inputInts, err := sliceAtoi(inputStrings)
	if err != nil {
		return nil, err
	}

	return inputInts, nil
}

// sliceAtoi is a utility function used to convert a slice of string representations of numbers
// to a slice of integers
func sliceAtoi(strings []string) ([]int, error) {
	ints := make([]int, len(strings))
	for i, s := range strings {
		c, err := strconv.Atoi(s)
		if err != nil {
			return nil, err
		}

		ints[i] = c
	}

	return ints, nil
}
