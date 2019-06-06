# Guess the Number Game
# 05/18
# Elliot Lister

import random as r
import time
import os

#########################################################
diffLevel = int(input("Choose a difficulty level(1-3): "))
num = r.randint(0,(diffLevel*10))
maxGuess = 5*diffLevel

print("Level", diffLevel, "Selected: Number is between 0 and 10")
print("You have", maxGuess, "guesses")

print(num)

guessNum = int(input("Guess a number: "))
guessesTaken = 1

while (guessNum != num) and (guessesTaken<maxGuess):
    
    if guessNum>num:
        print("Your guess was too high :((")

    elif guessNum<num:
        print("Your guess was too low :((")
        
    guessNum = int(input("Guess a number: "))
    guessesTaken = guessesTaken + 1
    guessesLeft = (maxGuess-guessesTaken)
    if guessNum == num:
        tense = "had"
    else:
        tense = "have"
    if guessesLeft >=2:
        print("You", tense, guessesLeft, "guesses left!")
    elif guessesLeft == 1:
         print("You", tense, "1 guess left!")
    else:
        print("Sorry you ran out of guesses!")
    

else:
    for letter in ("\nWELL DONE\n"):
            colorHex = hex(r.randint(0,255))
            os.system("color (colorHex)")
            time.sleep(0.15)
            print(letter)
