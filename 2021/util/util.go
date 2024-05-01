package util

import (
	"bytes"
	"errors"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	InputUrl      = "https://adventofcode.com/2021/day/%d/input"
	InputFilepath = "input/%d.input"
	InputTestFilepath = "input/%d.test.input"
)

// GetInput retrieves the input data for the given day from the downloaded input files.
// The data is returned as a byte slice and any read error encountered.
func GetInput(day int, test bool) ([]byte, error) {
	var input []byte
	var err error
	if test {
		input, err = os.ReadFile(fmt.Sprintf(InputTestFilepath, day))
	} else {
		input, err = os.ReadFile(fmt.Sprintf(InputFilepath, day))
	}
	if err != nil {
		return nil, err
	}

	return input, nil
}

// GetInputAsStrings retrieves the input data for the given day from the downloaded input files.
// The data is returned as a slice of strings divided by line and any read error encountered.
func GetInputAsStrings(day int, test bool) ([]string, error) {
	input, err := GetInput(day, test)
	if err != nil {
		return nil, err
	}

	inputStrings := strings.Split(strings.Trim(string(input), "\n \t"), "\n")

	return inputStrings, nil
}

// GetInputAsInts retrieves the input data for the given day from the downloaded input files.
// The data is returned as a slice of integers (given one number per line) and any read error encountered.
func GetInputAsInts(day int, test bool) ([]int, error) {
	inputStrings, err := GetInputAsStrings(day, test)
	if err != nil {
		return nil, err
	}

	inputInts, err := SliceAtoi(inputStrings)
	if err != nil {
		return nil, err
	}

	return inputInts, nil
}

func GetInputMultiDimensionalString(day int, test bool) ([][]string, error){
	input, err := GetInputAsStrings(day, test)
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

func GetInputMultiDimensionalByte(day int, split byte, test bool) ([][]byte, error){
	input, err := GetInput(day, test)
	if err != nil {
		return nil, err
	}

	s := bytes.TrimSpace(input)
	t := bytes.Split(s, []byte{split})

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

func Reflect2DSlice(in [][]byte, reverse bool) ([][]byte, error) {
	x := len(in)
	if x == 0 {
		return nil, errors.New("invalid input slice")
	}

	y := len(in[0])
	out := make([][]byte, y)

	for i := 0; i < y; i++ {
		t := make([]byte, x)
		for j := 0; j < x; j++ {
			t[j] = in[j][i]
		}
		out[i] = t
	}

	return out, nil
}

func Duplicate(data [][]byte) [][]byte {
	dupe := make([][]byte, len(data))
	for i := range data {
		dupe[i] = make([]byte, len(data[i]))
		copy(dupe[i], data[i])
	}

	return dupe
}

func Min(x, y int) int {
	if x < y {
		return x
	}

	return y
}

func Max(x, y int) int {
	if Min(x, y) == x {
		return y
	}

	return x
}
