import sys
import random

def guess_number():
    gn = ("1,2,3")

playerchoice = input ("\nGuess the number...\n1,\n2,or \n3\n\n")

if playerchoice not in ["1","2","3"]:
    print("please enter 1,2, or 3.")
