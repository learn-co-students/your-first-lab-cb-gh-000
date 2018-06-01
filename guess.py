import random as r

num = r.randint(0,20)
guessesTaken = 0
guessNum = int(input("Guess a number: "))

while guessNum != num:
    
    if guessNum>num:
        print("lower")
        guessNum = int(input("Guess a number: "))

    elif guessNum<num:
        print("higher")
        guessNum = int(input("Guess a number: "))

print("Well done")
