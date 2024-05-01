package day5

import (
	"aoc2021/util"
	"fmt"
	"strings"
)

type coord struct {
	x int
	y int
}

type line struct {
	a coord
	b coord
}

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
	input, err := getInput()
	if err != nil {
		return 0, err
	}

	countCross := make(map[coord]int)
	for _, l := range input {
		path := l.getCrossedPoints(false)
		for _, c := range path {
			countCross[c] += 1
		}
	}

	cnt := 0
	for _, i := range countCross {
		if i > 1 {
			cnt++
		}
	}

	return cnt, nil
}

func part2() (int, error) {
	input, err := getInput()
	if err != nil {
		return 0, err
	}

	countCross := make(map[coord]int)
	for _, l := range input {
		path := l.getCrossedPoints(true)
		for _, c := range path {
			countCross[c] += 1
		}
	}

	cnt := 0
	for _, i := range countCross {
		if i > 1 {
			cnt++
		}
	}

	return cnt, nil
}

func getInput() (lines []line, err error) {
	input, err := util.GetInputAsStrings(5, false)
	if err != nil {
		return nil, err
	}

	for _, l := range input {
		sc := strings.Split(l, " -> ")
		
		s0 := strings.Split(sc[0], ",")
		i0, err := util.SliceAtoi(s0)
		if err != nil {
			return nil, err
		}
		c0 := coord{x: i0[0], y: i0[1]}

		s1 := strings.Split(sc[1], ",")
		i1, err := util.SliceAtoi(s1)
		if err != nil {
			return nil, err
		}
		c1 := coord{x: i1[0], y: i1[1]}
		
		lines = append(lines, line{
			a: c0,
			b: c1,
		})
	}

	return lines, nil
}

func (l *line) getCrossedPoints(diagonal bool) (crossed []coord) {
	var v, a, b int
	var x bool
	if l.a.x == l.b.x {
		v = l.a.x
		a = util.Min(l.a.y, l.b.y)
		b = util.Max(l.a.y, l.b.y)
		x = true
	} else if l.a.y == l.b.y {
		v = l.a.y
		a = util.Min(l.a.x, l.b.x)
		b = util.Max(l.a.x, l.b.x)
		x = false
	} else if diagonal {
		var xs, ys []int
		if l.a.x < l.b.x {
			for i := l.a.x; i <= l.b.x; i++ {
				xs = append(xs, i)
			}
		} else {
			for i := l.a.x; i >= l.b.x; i-- {
				xs = append(xs, i)
			}
		}
		if l.a.y < l.b.y {
			for i := l.a.y; i <= l.b.y; i++ {
				ys = append(ys, i)
			}
		} else {
			for i := l.a.y; i >= l.b.y; i-- {
				ys = append(ys, i)
			}
		}

		for i := 0; i < len(xs); i++ {
			crossed = append(crossed, coord{xs[i], ys[i]})
		}
		return crossed
	} else {
		return crossed
	}

	for i := a; i <= b; i++ {
		var t coord
		if x {
			t = coord{v, i}
		} else {
			t = coord{i, v}
		}

		crossed = append(crossed, t)
	}

	return crossed
}
