package day3

import (
	"aoc2021/util"
	"bytes"
	"errors"
	"fmt"
	"strconv"
)

const byteOne = '1'
const byteZero = '0'

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
	input, err := util.GetInputMultiDimensionalByte(3, '\n')
	if err != nil {
		return 0, err
	}

	input, err = util.Reflect2DSlice(input, false)
	if err != nil {
		return 0, err
	}

	var gamma, epsilon []byte
	for i, col := range input {
		mcb := findMostCommon(col)
		lcb := findLeastCommon(col)
		if mcb == 0 || lcb == 0 {
			return 0, errors.New(fmt.Sprintf("no common bit in col %d", i))
		}

		gamma = append(gamma, mcb)
		epsilon = append(epsilon, lcb)
	}


	i, err := strconv.ParseUint(string(gamma), 2, 0)
	if err != nil {
		return 0, err
	}

	j, err := strconv.ParseUint(string(epsilon), 2, 0)
	if err != nil {
		return 0, err
	}

	return int(i*j), nil
}

func part2() (int, error) {
	input, err := util.GetInputMultiDimensionalByte(3, '\n')
	if err != nil {
		return 0, err
	}

	inputR, err := util.Reflect2DSlice(input, false)
	if err != nil {
		return 0, err
	}

	oxy := util.Duplicate(input)
	co2 := util.Duplicate(input)

	for i := 0; i < len(inputR); i++ {
		oxyR, _ := util.Reflect2DSlice(oxy, false)
		co2R, _ := util.Reflect2DSlice(co2, false)

		rmOxy := findLeastCommon(oxyR[i])
		rmCo2 := findMostCommon(co2R[i])

		if rmOxy == 0 {
			 rmOxy = byteZero
		}

		if rmCo2 == 0 {
			rmCo2 = byteOne
		}

		for len(oxy) > 1 && bytes.Contains(oxyR[i], []byte{rmOxy}) {
			n := bytes.IndexByte(oxyR[i], rmOxy)
			oxy = append(oxy[:n], oxy[n+1:]...)
			oxyR[i] = append(oxyR[i][:n], oxyR[i][n+1:]...)
		}

		for len(co2) > 1 && bytes.Contains(co2R[i], []byte{rmCo2}) {
			n := bytes.IndexByte(co2R[i], rmCo2)
			co2 = append(co2[:n], co2[n+1:]...)
			co2R[i] = append(co2R[i][:n], co2R[i][n+1:]...)
		}
	}

	oxyInt, err := strconv.ParseUint(string(oxy[0]), 2, 0)
	if err != nil {
		return 0, err
	}

	co2Int, err := strconv.ParseUint(string(co2[0]), 2, 0)
	if err != nil {
		return 0, err
	}

	return int(oxyInt*co2Int), nil
}

func findMostCommon(bits []byte) byte {
	cntOne := bytes.Count(bits, []byte{byteOne})
	cntZero := bytes.Count(bits, []byte{byteZero})

	if cntOne > cntZero {
		return byteOne
	} else if cntZero > cntOne {
		return byteZero
	} else {
		return 0
	}
}

func findLeastCommon(bits []byte) byte {
	mcb := findMostCommon(bits)

	if mcb == byteZero {
		return byteOne
	} else if mcb == byteOne {
		return byteZero
	} else {
		return 0
	}
}
