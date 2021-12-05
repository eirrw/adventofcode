package main

import (
	"aoc2021/day1"
	"aoc2021/day2"
	"aoc2021/day3"
	"aoc2021/day4"
	"aoc2021/day5"
	"aoc2021/util"
	"errors"
	"fmt"
	"io"
	"log"
	"net/http"
	"net/http/cookiejar"
	"os"
	"strconv"
	"time"
)


func main() {
	if len(os.Args) == 3 {
		day, err := strconv.Atoi(os.Args[2])
		if err != nil {
			log.Fatal(err)
		}

		switch os.Args[1] {
		case "run":
			err = run(day)
		case "get":
			err = get(day)
		}

		if err != nil {
			log.Fatal(err)
		}
	} else {
		log.Fatal("Day number required")
	}
}

func run(day int) error {
	var err error
	switch day {
	case 1:
		err = day1.Run()
	case 2:
		err = day2.Run()
	case 3:
		err = day3.Run()
	case 4:
		err = day4.Run()
	case 5:
		err = day5.Run()
	}

	if err != nil {
		return err
	}

	return nil
}

func get(day int) error {
	var client http.Client
	jar, err := cookiejar.New(nil)
	if err != nil {
		return err
	}
	client = http.Client{
		Jar: jar,
	}

	expires, err := time.Parse(time.RFC1123, "Sat, 29 Nov 2031 17:31:10 GMT")
	if err != nil {
		return err
	}

	cookie := &http.Cookie{
		Name: "session",
		Value: os.Getenv("AOC_SESSION"),
		Expires: expires,
	}

	url := fmt.Sprintf(util.InputUrl, day)
	req, err := http.NewRequest(http.MethodGet, url, nil)
	if err != nil {
		return err
	}

	req.AddCookie(cookie)

	resp, err := client.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode == 200 {
		out, err := os.Create(fmt.Sprintf(util.InputFilepath, day))
		if err != nil {
			return err
		}
		defer out.Close()

		_, err = io.Copy(out, resp.Body)
		if err != nil {
			return err
		}
	} else {
		body, err := io.ReadAll(resp.Body)
		if err != nil {
			return err
		}

		_, err = os.Stderr.Write(body)
		if err != nil {
			return err
		}

		return errors.New(http.StatusText(resp.StatusCode))
	}

	return nil
}
