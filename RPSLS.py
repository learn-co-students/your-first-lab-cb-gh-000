# RPSLS
# 05/18
# Elliot Lister
import random as r
import time



gameNum = 0
pointTotal = 0
compTotal = 0
while gameNum!=5:
            choice = input("1. Rock\n"
                   "2. Paper\n"
                   "3. Scissors\n"
                   "4. Lizard\n"
                   "5. Spock\n"
                   "Pick an option: ")
            gameNum = gameNum+1
            compChoice = r.randint(1,4)
            options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
            print("The computer chose: " + str(options[compChoice]) + "!")
            if choice == '1' or choice == 'Rock':
                        if compChoice == 1:
                                    print("\nDraw!\nNo points added\n.")
                                    
                        elif compChoice == 3 or compChoice == 4:
                                    print("\nYou win!\n\n+1 Point.\n")
                                    pointTotal = pointTotal + 1
                                    
                        elif compChoice == 2 or compChoice == 5:
                                    print("\nYou lose!\n\n+1 Point to the Computer.\n")
                                    compTotal = compTotal + 1

            if choice == '2' or choice == 'Paper':
                        if compChoice == 2:
                                    print("\nDraw!\nNo points added\n.")
                                    
                        elif compChoice == 1 or compChoice == 5:
                                    print("\nYou win!\n\n+1 Point.\n")
                                    pointTotal = pointTotal + 1
                                    
                        elif compChoice == 3 or compChoice == 4:
                                    print("\nYou lose!\n\n+1 Point to the Computer.\n")
                                    compTotal = compTotal + 1

            if choice == '3' or choice == 'Scissors':
                        if compChoice == 3:
                                    print("\nDraw!\nNo points added\n.")
                                    
                        elif compChoice == 4 or compChoice == 2:
                                    print("\nYou win!\n\n+1 Point.\n")
                                    pointTotal = pointTotal + 1
                                    
                        elif compChoice == 1 or compChoice == 5:
                                    print("\nYou lose!\n\n+1 Point to the Computer.\n")
                                    compTotal = compTotal + 1

            if choice == '4' or choice == 'Lizard':
                        if compChoice == 4:
                                    print("\nDraw!\nNo points added\n.")
                                    
                        elif compChoice == 3 or compChoice == 4:
                                    print("\nYou win!\n\n+1 Point.\n")
                                    pointTotal = pointTotal + 1
                                    
                        elif compChoice == 2 or compChoice == 5:
                                    print("\nYou lose!\n\n+1 Point to the Computer.\n")
                                    compTotal = compTotal + 1

            if choice == '5' or choice == 'Spock':
                        if compChoice == 5:
                                    print("\nDraw!\nNo points added\n.")
                                    
                        elif compChoice == 1 or compChoice == 3:
                                    print("\nYou win!\n\n+1 Point.\n")
                                    pointTotal = pointTotal + 1
                                    
                        elif compChoice == 2 or compChoice == 4:
                                    print("\nYou lose!\n\n+1 Point to the Computer.\n")
                                    compTotal = compTotal + 1

print("You scored: " + str(pointTotal) + " points!\n"
      "The computer scored: " + str(compTotal) + " points!\n")

if pointTotal>compTotal:
            for letter in ("\nYOU WIN\n"):
                        time.sleep(0.15)
                        print(letter)

if pointTotal<compTotal:
            for letter in ("\nYOU LOSE\n"):
                        time.sleep(0.15)
                        print(letter)

if pointTotal == compTotal:
            print("\'Twas a draw")
            

                            
                

