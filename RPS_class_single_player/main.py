import Player as pp
import Computer as cc

def intro():
    text = "Welcome to my Rock Paper Scissors game!"
    header = "#"*len(text)
    print(header)
    print(text)

def new_game():
    global set_round
    text = "Play new game (y/n)? "
    choice = input(text).lower()
    if choice == "y":
        set_round = round_settings()
        play_game(set_round)
    elif choice == "n":
        print("See ya!")
    else:
        invalid_input()
        new_game()

def round_settings():
    text = "\nHow many rounds do you want to play? "
    try:
        choice = int(input(text))
    except ValueError as msg:
        invalid_input()
        print(str(msg))
        round_settings()
    return choice

def play_game(rounds):
    for i in range(rounds):
        rps_winner()
    play_again()  

def rps_winner():
    display = {"r" : "rock", "p" : "paper", "s" : "scissors"}
    player_choice = player.choice()
    computer_choice = computer.choice()
    if player_choice == computer_choice:
        text = "\nIt was a tie! You both moved: {}\n".format(display[player_choice])
        print(text)
        stats()
    elif (player_choice == "r" and computer_choice == "s") or \
        (player_choice == "p" and computer_choice == "r") or \
        (player_choice == "s" and computer_choice == "p"):
        text = "\nYou won! You moved: {}\nThe computer moved: {}".format(display[player_choice],display[computer_choice])
        print(text)
        player.score += 1
        if computer.score >= 1:
            computer.score -= 1
        stats()
    elif player_choice not in cc.Computer.valid_moves:
        invalid_input()
        rps_winner()        
    else:
        text = "\nYou lost! You moved: {}\nThe computer moved: {}".format(display[player_choice], display[computer_choice])
        print(text)
        if player.score >= 1:
            player.score -= 1
        computer.score += 1
        stats()

def stats():
    print("\n" + "Score Table".center(50, "-"))
    player.show_score()
    computer.show_score()

def play_again():
    text = "\nPlay again (y/n)? "
    choice = input(text).lower()
    if choice == "y":
        load_settings()
    elif choice == "n":
        print("See ya!")
    else:
        invalid_input()
        play_again()

def load_settings():
    text = "Do you want to load previous round settings (y/n)? "
    choice = input(text).lower()
    if choice == "n":
        _set_round = round_settings()
        reset_scores()
        play_game(_set_round)
    elif choice == "y":
        reset_scores()
        play_game(set_round)
    else:
        invalid_input()
        load_settings()

def reset_scores():
    text = "Do you wish to reset the previous scores (y/n)? "
    choice = input(text).lower()
    if choice == "n":
        pass
    elif choice == "y":
        player.score = 0
        computer.score = 0
    else:
        invalid_input()
        reset_scores()

def invalid_input():
    text = "Invalid Input!"
    print("\n" + "!"*len(text)*2)
    print(text)
    print("!"*len(text)*2 + "\n")

if __name__ == "__main__":
    intro()
    player = pp.Player()
    computer = cc.Computer()
    new_game()


