import random as r
guessesTaken = 0

diffLevel = int(input("Choose a difficulty level(1-3): "))

if diffLevel == 1:
    num = r.randint(0,10)
    print("Level 1 Selected: Number is between 0 and 10")
    maxGuess = 5

elif diffLevel == 2:
    num = r.randint(0,50)
    print("Level 2 Selected: Number is between 0 and 50")
    maxGuess = 7

elif diffLevel == 3:
    num = r.randint(0,100)
    print("Level 3 Selected: Number is between 0 and 100")
    maxGuess = 15

guessNum = int(input("Guess a number: "))

while (guessNum != num) and (guessesTaken<maxGuess):
    
    if guessNum>num:
        print("Your guess was too high :((")
        guessNum = int(input("Guess a number: "))
        guessesTaken = guessesTaken + 1

    elif guessNum<num:
        print("Your guess was too low :((")
        guessNum = int(input("Guess a number: "))
        guessesTaken = guessesTaken + 1


print("Well done")
