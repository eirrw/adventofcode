package day4

import (
	"aoc2021/util"
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

type cell struct {
	value int
	marked bool
}

type bingo struct {
	board [][]cell
	won bool
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
	draw, boards, err := getInput()
	if err != nil {
		return 0, err
	}

	var score int
	for _, num := range draw {
		for _, board := range boards {
			board.mark(num)
			if board.checkWin() {
				score = board.getScore() * num
				return score, nil
			}
		}
	}

	return 0, nil
}

func part2() (int, error) {
	draw, boards, err := getInput()
	if err != nil {
		return 0, err
	}

	for _, num := range draw {
		done := make([]int, 0)
		for i, board := range boards {
			board.mark(num)
			if board.checkWin() && len(boards) == 1 {
				return board.getScore() * num, nil
			} else if board.won {
				done = append(done, i)
			}
		}

		sort.Sort(sort.Reverse(sort.IntSlice(done)))
		for _, k := range done {
			boards[k] = boards[len(boards)-1]
			boards = boards[:len(boards)-1]
		}
	}

	return 0, nil
}

func getInput() (draw []int, boards []bingo, err error) {
	file, err := os.Open(fmt.Sprintf(util.InputFilepath, 4))
	if err != nil {
		return nil, nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var tmpBoard [][]cell
	for scanner.Scan() {
		line := scanner.Text()
		if strings.ContainsRune(line, ',') {
			draw, err = util.SliceAtoi(strings.Split(line, ","))
			if err != nil {
				return nil, nil, err
			}

			continue
		}

		if len(line) > 0 {
			line = strings.ReplaceAll(line, "  ", " ")
			line = strings.TrimSpace(line)
			ints, err := util.SliceAtoi(strings.Split(line, " "))
			if err != nil {
				return nil, nil, err
			}

			var t []cell
			for _, v := range ints {
				t = append(t, cell{v, false})
			}

			tmpBoard = append(tmpBoard, t)
		}

		if len(tmpBoard) == 5 {
			boards = append(boards, bingo{tmpBoard, false})
			tmpBoard = nil
		}
	}

	return draw, boards, nil
}

func (b *bingo) mark(num int) {
	for i, row := range b.board {
		for j, c := range row {
			if c.value == num {
				b.board[i][j].marked = true
			}
		}
	}
}

func (b *bingo) checkWin() bool {
	if b.won {
		return true
	}

	var markCntRow int
	var markCntCol int
	for i := 0; i < len(b.board); i++ {
		for j := 0; j < len(b.board[i]); j++ {
			if b.board[i][j].marked {
				markCntRow++
			}
			if b.board[j][i].marked {
				markCntCol++
			}
		}

		if markCntRow == 5 || markCntCol == 5 {
			b.won = true
			return true
		} else {
			markCntCol, markCntRow = 0, 0
		}
	}

	return false
}

func (b *bingo) getScore() (score int) {
	for _, row := range b.board {
		for _, c := range row {
			if !c.marked {
				score += c.value
			}
		}
	}

	return
}
