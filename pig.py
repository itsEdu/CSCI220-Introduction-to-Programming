# Name: Eduardo R Abreu
# pig.py
#
# Problem: This program is a chance based game between a computer and
#          a player.
#
# Certification of Authenticity:  
# I certify that this lab is entirely my own work.

from random import *
from sys import exit

def roll():
    return randint(1, 6)
    
def playerPlays(totalPlayerPoints):
    roundPoints = 0
    firstRoll = 0
    secondRoll = 0
    play = "y"
    while firstRoll != 1 and secondRoll != 1 and play == "y":
        firstRoll = roll()
        secondRoll = roll()
        print("You rolled a " + str(firstRoll) + " and " + str(secondRoll))
        if firstRoll != 1 and secondRoll != 1:
            roundPoints = roundPoints + firstRoll + secondRoll
        else:
            roundPoints = 0
        print("This round's points: " + str(roundPoints))
        if firstRoll != 1 and secondRoll != 1:
            play = input("Do you want to play again? (Y/N) ").lower()
        print()
    if firstRoll == 1 and secondRoll == 1:
        print("Ouch! Snake eyes.")
        totalPoints = 0
    elif firstRoll == 1 or secondRoll == 1:
        totalPoints = totalPlayerPoints
    else:
        totalPoints = totalPlayerPoints + roundPoints
    print("-----------------------------------------------------------")
    return totalPoints
    
def computerPlays(compPoints):
    roundPoints = 0
    firstRoll = 0
    secondRoll = 0
    while firstRoll != 1 and secondRoll != 1 and roundPoints < 20:
        firstRoll = roll()
        secondRoll = roll()
        print("Computer rolled a " + str(firstRoll) + " and " + str(secondRoll))
        if firstRoll != 1 and secondRoll != 1:
            roundPoints = roundPoints + firstRoll + secondRoll
        else:
            roundPoints = 0
        print("Computer round points: " + str(roundPoints))
        print()
    if firstRoll == 1 and secondRoll == 1:
        print("Ouch! Snake eyes.")
        totalPoints = 0
    elif firstRoll == 1 or secondRoll == 1:
        totalPoints = compPoints
    else:
        totalPoints = compPoints + roundPoints
    print("-----------------------------------------------------------")
    return totalPoints
    
def playPig():
    play = "y"
    while play == "y":
        print("Welcome to 'Pig'!")
        print("Pig is a PvE game. Two dice are rolled ", end ="")
        print("and chance determines your score!")
        print("-----------------------------------------------------------")
        playerPoints = 0
        compPoints = 0
        while playerPoints < 100 and compPoints < 100:
            playerPoints = playerPlays(playerPoints)
            if playerPoints < 100:
                compPoints = computerPlays(compPoints)
        if playerPoints > compPoints:
            print("You win!")
            print("Computer total points: " + str(compPoints))
            print("Your total points: " + str(playerPoints))
        else:
            print("The computer wins!")
            print("Computer total points: " + str(compPoints))
            print("Your total points: " + str(playerPoints))
        print("Thank you for playing pig!")
        play = input("Do you want to play again? (Y/N) ").lower()
        print("\n" * 2)
    if play == "n":
        exit(0)
    
def main():
    playPig()

main()
