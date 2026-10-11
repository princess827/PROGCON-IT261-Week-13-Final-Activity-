#FULL CODE OF THE GAME

import random
def playGame(difficulty):
    if difficulty == 1:
        maxNumber = 10
    else:
        if difficulty == 2:
            maxNumber = 50
        else:
            if difficulty == 3:
                maxNumber = 100
            else:
                print("Pick a valid option")
    secretNumber = int(random.random() * maxNumber) + 1
    attempts = 0
    while True:    #This simulates a Do Loop
        print("Enter your guess (1 to " + str(maxNumber) + "):")
        guess = int(input())
        attempts = attempts + 1
        if guess < secretNumber:
            print("Too low! Try Again")
        else:
            if guess > secretNumber:
                print("Too high! Try again")
        if guess == secretNumber: break
    print("Correct! You got it in " + str(attempts) + " tries.")

# Main
while True:    #This simulates a Do Loop
    print("Select Difficulty: 1(easy), 2(medium), 3(hard)")
    difficulty = int(input())
    playGame(difficulty)
    print("Play Again? (Y/N)")
    playAgain = input()
    if playAgain != "Y" and playAgain != "y": break
print("Thank you for playing!")
