#!/usr/lib/env python3

import random

def intro():
    text = "Welcome to ROCK, PAPER, SCISSORS game!\n"
    header = "#"*len(text)
    print(header)
    print(text)
    continue_game()

def continue_game():
    text = input("Do you wish to play or continue playing (y/n)? ").lower()
    if text == "y":
        play_Game()
    elif text == "n":
        print("\nThank you for playing!\n")
    else:
        invalid_input()
        continue_game()

def invalid_input():
    text = "You can only input y or n"
    print("\n" + "!"*len(text)*2)
    print(text)
    print("!"*len(text)*2 + "\n")

def rps_winner(player, computer):
    if player == computer:
        print("\nIt was a tie! You both moved: {}\n".format(display[player]))
        continue_game()
    elif (player == "r" and computer == "s") or \
        (player == "p" and computer == "r") or \
        (player == "s" and computer == "p"):
        print("\nYou won! You moved: {} | The computer moved: {}\n".format(display[player], display[computer]))
        continue_game()
    elif player not in valid_moves:
        invalid_input()
        play_Game()
    else:
        print("\nYou lost! You moved: {} | The computer moved: {}\n".format(display[player], display[computer]))
        continue_game()

def play_Game():
    text = "\nEnter (r)ock, (p)aper, (s)cissors: "
    print("="*len(text))
    player = input(text).lower()
    computer = random.choice(valid_moves)
    rps_winner(player, computer)

if __name__ == "__main__":
    valid_moves = ["r", "p", "s"]
    display = {"r" : "rock", "p" : "paper", "s" : "scissors"}
    intro()


