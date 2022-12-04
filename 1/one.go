package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func load_file(name string) (string, error) {
	bytes, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("error reading file. Error: " + err.Error())
		return "", fmt.Errorf("")
	}

	return string(bytes), nil
}

func parse_input(raw_input string) (res [][]int) {
	split_input := strings.Split(raw_input, "\n")

	temp := make([]int, 0)
	for i := 0; i < len(split_input); i++ {
		line := split_input[i]
		if line == "" {
			res = append(res, temp)
			temp = make([]int, 0)
			continue
		}

		cal, _ := strconv.Atoi(line)
		temp = append(temp, cal)
	}
	return
}

func main() {
	raw_input, err := load_file("./input1.txt")
	if err != nil {
		return
	}

	parsed_elf_contents := parse_input(raw_input)

	result := 0
	for _, list := range parsed_elf_contents {
		sum := 0
		for _, cal := range list {
			sum += cal
		}

		if sum > result {
			result = sum
		}
	}

	fmt.Println(result)
}
