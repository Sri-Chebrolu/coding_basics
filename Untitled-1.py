# Code game rock paper scissors

# import libraries
import random, sys

print("Welcome to the game of Rock, Paper, Scissors!")

# define the game function
def game():

    # define game options
    game_options = ["rock", "paper", "scissors"]

    # define game score and starting score

    wins = 0
    losses = 0
    ties = 0

    user = input("Enter your move: (r)ock, (p)aper, or (s)cissors or (q)uit: ")

    if user == "q":
        print("Thanks for playing!")
        sys.exit()

    if user not in game_options:
        print("Invalid move. Please try again.")
        return

    computer = random.choice(game_options)

    print(f"You chose {user}, computer chose {computer}.")

    def play_again():

        print("Do you want to play again")
        user = input("Enter (y)es or (n)o: ")

        if user == "y":
            return

        elif user == "n":
            print("Okay, let me know when you want to play!")
            return

    if user == computer:
        print("It's a tie!")
        ties = ties + 1
        play_again()

    elif user == "r" and computer != "paper":
        print("You won!")
        wins = wins + 1
        
    elif user == "p" and computer != "scissors":
        print("You won!")
        wins = wins + 1
        
    elif user == "s" and computer != "rock":
        print("You won!")
        wins = wins + 1

    else:
        print("You lost!")
        losses = losses + 1
        play_again()


