# Main
while True:    #This simulates a Do Loop
    print("Select Difficulty: 1(easy), 2(medium), 3(hard)")
    difficulty = int(input())
    playGame(difficulty)
    print("Play Again? (Y/N)")
    playAgain = input()
    if playAgain != "Y" and playAgain != "y": break
print("Thank you for playing!")
