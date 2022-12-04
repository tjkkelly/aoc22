package main

import (
	"fmt"
	"os"
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

func parse_input(raw_input string) (res [][]string) {
	raw_input = strings.Trim(raw_input, "\n")
	split_input := strings.Split(raw_input, "\n")

	for i := 0; i < len(split_input); i++ {
		line := split_input[i]
		split_line := strings.Split(line, " ")

		res = append(res, split_line)
	}

	return
}

// First Column
// A -> Rock
// B -> Paper
// C -> Scissors

// Second column
// X -> Rock
// Y -> Paper
// Z -> Scissors

func score_round(opponent_move string, my_move string) (opponent_score int, my_score int) {
	opponent_translate_map := map[string]string{
		"A": "rock",
		"B": "paper",
		"C": "scissors",
	}
	my_translate_map := map[string]string{
		"X": "rock",
		"Y": "paper",
		"Z": "scissors",
	}

	rank_map := map[string]string{
		"rock":     "scissors",
		"scissors": "paper",
		"paper":    "rock",
	}

	choice_score_map := map[string]int{
		"rock":     1,
		"paper":    2,
		"scissors": 3,
	}

	opponent_move_translated := opponent_translate_map[opponent_move]
	my_move_translated := my_translate_map[my_move]

	opponent_score = choice_score_map[opponent_move_translated]
	my_score = choice_score_map[my_move_translated]

	// is it a tie?
	if opponent_move_translated == my_move_translated {
		opponent_score += 3
		my_score += 3
	} else if rank_map[my_move_translated] == opponent_move_translated { // I won
		my_score += 6
	} else if rank_map[opponent_move_translated] == my_move_translated {
		opponent_score += 6
	} else {
		panic("invalid condition")
	}

	return
}

func process_rounds(rounds [][]string) (opponent_score_final int, my_score_final int) {
	for _, round := range rounds {
		opponent_move := round[0]
		my_move := round[1]

		opponent_score, my_score := score_round(opponent_move, my_move)

		opponent_score_final += opponent_score
		my_score_final += my_score
	}

	return
}

func main() {
	raw_input, err := load_file("./input1.txt")
	if err != nil {
		return
	}

	parsed_input := parse_input(raw_input)
	opponent_score_final, my_score_final := process_rounds(parsed_input)

	fmt.Print("opponent final: ")
	fmt.Println(opponent_score_final)
	fmt.Print("my final: ")
	fmt.Println(my_score_final)
	fmt.Println("complete")
}
