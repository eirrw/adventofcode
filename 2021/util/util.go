package util

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	InputUrl      = "https://adventofcode.com/2021/day/%d/input"
	InputFilepath = "input/%d.input"
)

// GetInput retrieves the input data for the given day from the downloaded input files.
// The data is returned as a byte slice and any read error encountered.
func GetInput(day int) ([]byte, error) {
	input, err := os.ReadFile(fmt.Sprintf(InputFilepath, day))
	if err != nil {
		return nil, err
	}

	return input, nil
}

// GetInputAsStrings retrieves the input data for the given day from the downloaded input files.
// The data is returned as a slice of strings divided by line and any read error encountered.
func GetInputAsStrings(day int) ([]string, error) {
	input, err := GetInput(day)
	if err != nil {
		return nil, err
	}

	inputStrings := strings.Split(strings.Trim(string(input), "\n \t"), "\n")

	return inputStrings, nil
}

// GetInputAsInts retrieves the input data for the given day from the downloaded input files.
// The data is returned as a slice of integers (given one number per line) and any read error encountered.
func GetInputAsInts(day int) ([]int, error) {
	inputStrings, err := GetInputAsStrings(day)
	if err != nil {
		return nil, err
	}

	inputInts, err := SliceAtoi(inputStrings)
	if err != nil {
		return nil, err
	}

	return inputInts, nil
}

func GetInputMultiDimensional(day int) ([][]string, error){
	input, err := GetInputAsStrings(day)
	if err != nil {
		return nil, err
	}

	var t [][]string
	for _, s := range input {
		sub := strings.Split(s, " ")
		t = append(t, sub)
	}

	return t, nil
}

// SliceAtoi is a utility function used to convert a slice of string representations of numbers
// to a slice of integers
func SliceAtoi(strings []string) ([]int, error) {
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
