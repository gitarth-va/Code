# First Challenge
# October 1, 2020
# Author: Hitarth Patel
# 
# Objective: Given a stream of elements too large to store in memory. Pick a ran# random element from the stream with uniform probability
import random

def getCharacter(theString):
    "Function will take givenString as an input and return a random character from that string"
    try:
        finalChar = random.choice(theString)
        # Check for if the choice is empty
        while finalChar.isspace() or len(finalChar) == 0:
            finalChar = random.choice(theString)

        return print(f"The random character is {finalChar}")
    except IndexError:
        # print(err)
        print("Can't pick from empty string, try again.")
    

if __name__ == "__main__":
    while True:

        givenString = input("Please enter a String:\t")
        if givenString.isspace():
            print("String cannot be just spaces.")
            break
        getCharacter(givenString)


