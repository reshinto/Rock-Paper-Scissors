class Player:
    num_of_players = 0
    def __init__(self):
        Player.num_of_players += 1
        choice = input("Do you want to register your name (y/n)? ").lower()
        if choice == "y":
            self.name = input("Enter Player {} name: ".format(Player.num_of_players))
        elif choice == "n":
            self.name = "Player {}".format(Player.num_of_players)
        else:
            print("You have entered an invalid input! Player name will be set to default!!")
            self.name = "Player {}".format(Player.num_of_players)
        self.score = 0

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def show_score(self):
        print("{}".format(self.name).ljust(20, " ") + "\t|\tScore: {}".format(str(self.score)))

    def choice(self):
        print("\n" + "{}'s turn".format(self.name).center(80, "#"))
        text = "Choose your move!\n(r)ock, (p)aper, (s)cissors"
        self.player_choice = input("{}: {}\n> ".format(self.name, text)).lower()
        return self.player_choice