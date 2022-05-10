#Rock Paper Scissors Game

import random

#Function to check the winner of the game
def check_winner(choice, c_choice):
    #Checking if it's a tie between both the players
    if choice == c_choice:
        print("Both players selected {}. It's a tie!".format(choice))
    elif choice == "paper":
        if c_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose. Better luck next time.")
    elif choice == "rock":
        if c_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose. Better luck next time.")
    elif choice == "scissors":
        if c_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose. Better luck next time.")

#Main Function
def main():
    print(":: Let's Play Rock, Paper, Scissors! ::")
    while (str.lower(input("Enter 'y' or 'Y' to play, any other key to exit: ")) == 'y'):
        action = input("Enter your choice (rock, paper, scissors) -->  ")
        choices = ["rock", "paper", "scissors"]
        c_action = random.choice(choices)
        print(f"\nYou chose {action} & computer chose {c_action}.\n")
        check_winner(action,c_action)
    print("Thanks for playing!")

if __name__ == '__main__':
    main()