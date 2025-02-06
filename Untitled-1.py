# Code game rock paper scissors

# import libraries
import random, sys

print("Welcome to the game of Rock, Paper, Scissors!")

# define function to restart or quit game
def play_again():

            print("Do you want to play again")
            user = input("Enter (y)es or (n)o: ")

            if user == "y":
                return True
            elif user == "n":
                print("Okay, let me know when you want to play!")
                return False
            else:
                return print("Invalid input. Please enter 'y' or 'n'.")
                

# define the game function
def game():

    # define game options
    game_options = ["r", "p", "s"]

    # define game score and starting score

    wins = 0
    losses = 0
    ties = 0

    playing = True
    while playing:

        user = input("Enter your move: (r)ock, (p)aper, or (s)cissors or (q)uit: ")

        if user == "q":
            print("Thanks for playing!")
            sys.exit()

        if user not in game_options:
            print("Invalid move. Please try again.")
            continue

        computer = random.choice(game_options)

        print(f"You chose {user}, computer chose {computer}.")

        if user == computer:
            print("It's a tie!")
            ties += 1
        elif [(user == "r" and computer != "p") | (user == "p" and computer != "s") | (user == "s" and computer != "r")] :
            print("You won!")
            wins += 1
        else:
            print("You lost!")
            losses += 1
            
        playing = play_again()

    return print("Thanks for playing")

game()



    


