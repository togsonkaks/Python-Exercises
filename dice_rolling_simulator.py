#Rolling Dice Simulator
import random

#Function to roll a Dice
def roll_dice():
    #Choices present in a Dice
    choices = [1,2,3,4,5,6]
    #Selecting a random choice from the choices list
    number = random.choice(choices)
    #Return the randomly selected choice
    return number

#Main Function
def main():
    print(":: Rolling Dice Simulator ::")
    while (str.lower(input("Do you want to roll a dice? Enter 'y' or 'Y' to roll, any other key to exit: ")) == 'y'):
        print("Rolling a Dice..")
        num = roll_dice()
        print("Dice is Rolled. Number is {}".format(num))
    print("Exiting now..")
    exit()

if __name__ == '__main__':
    main()