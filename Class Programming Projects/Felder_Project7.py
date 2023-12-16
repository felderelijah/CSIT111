# Elijah Felder
# 11/05/23
# Programming Project 7
# rolling dice game using the random function
# whatever player has the higher value determines the winner

import random

# this function will get the player names
def getNames():
    global name1
    global name2
    name1 = input('Player 1, enter your name: ')
    name2 = input('Player 2, enter your name: ')
    
# this function will get the random values
def rolldie():
    rolled = random.randint(1,6)
    return(rolled)

# this function will display the winner
def winner():
    
    if player1 > player2:
        print(name1.capitalize(), "rolled a number higher than", name2.capitalize())
        print("Player 1 wins!")
    elif player2 > player1:
        print(name2.capitalize(), "rolled a number higher than", name1.capitalize())
        print("Player 2 wins!")
    else:
        print("You both tied")
        
# start the program by calling the main module
def main():

    # initialize variables
    game = "rolling dice game"
    print("       ", game.upper())
    print("-------------------------------------\n")

    # call to the inputNames function
    getNames()
    endProgram = 'no'

    # while loop to run the program repeatedly
    while endProgram != 'yes':

        # initialize variables
        global player1 
        global player2

        # call to the rollDice function
        player1 = rolldie()
        print('\nPlayer 1 rolled a', player1)
        player2 = rolldie()
        print('Player 2 rolled a', player2, '\n')

         # call to the displayInfo function
        winner()

        # end the while loop or restart the program
        endProgram = input('Do you want to end the program? (Enter yes or no): ')
    print("\nThanks for playing")

# the end of main module
main()
