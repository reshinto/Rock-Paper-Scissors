import random

class Computer:
    num_of_com_players = 0
    valid_moves = ["r", "p", "s"]
    def __init__(self):
        Computer.num_of_com_players += 1
        text = "Do you want to set computer name as default (y/n)? "
        choice = input(text).lower()
        if choice == "y":
            self.name = "Computer {}".format(Computer.num_of_com_players)
        elif choice == "n":
            self.name = input("Enter Computer {} name: ".format(Computer.num_of_com_players))
        else:
            print("You have entered an invalid input! Computer name will be set to default!!")
            self.name = "Computer {}".format(Computer.num_of_com_players)
        self.score = 0

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def show_score(self):
        print("{}".format(self.name).ljust(20, " ") + "\t|\tScore: {}".format(str(self.score)))

    def choice(self):
        self.com_choice = random.choice(Computer.valid_moves)
        return self.com_choice