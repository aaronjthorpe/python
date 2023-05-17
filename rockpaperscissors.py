"""
Rock, Paper, Scissors CLI Game
rockpaperscissors.py
Aaron Thorpe
10/5/2023
aaron.thorpe@academyit.com.au

This game ask the user to choose rock, paper, or scissors.
The computer will then make it's own move.
The game will determine who won the game or if it was a draw.

The game will continue until the user quits by pressing 'q'.
"""

#import modules
import random

#Title
print("Rock, paper, scissors game!!!\n")

#Start game loop
while True:

    #Gather player data
    playerMove = input("For Rock type      r\nFor Paper type     p\nFor Scissors type  s\nTo Quit type       q\n\nWhat's your move?\n").lower()

    if playerMove == 'q':
        break
    
    #Calculate Computer Move
    listOfMvoes = ['r','p','s']
    computerRandomNumber = random.randint(0,2)
    computerMove = listOfMvoes[computerRandomNumber]

    #Win / Lose / Draw logic
    if playerMove == 'r' and computerMove == 's':
        result = 'win'
    elif playerMove == 's' and computerMove == 'p':
        result = 'win'
    elif playerMove == 'p' and computerMove == 'r':
        result = 'win'
    elif playerMove == 'r' and computerMove == 'p':
        result = 'lose'
    elif playerMove == 's' and computerMove == 'r':
        result = 'lose'
    elif playerMove == 'p' and computerMove == 's':
        result = 'lose'
    else:
        result = 'draw' 

    #create user-friendly output format for moves (optional!)
    if playerMove == 'r':
        playerMove = 'Rock'
    if playerMove == 's':
        playerMove = 'Scissors'
    if playerMove == 'p':
        playerMove = 'Paper'
    if computerMove == 'r':
        computerMove = 'Rock'
    if computerMove == 's':
        computerMove = 'Scissors'
    if computerMove == 'p':
        computerMove = 'Paper'
    
    #output moves
    print("You chose",playerMove)
    print("The computer chose",computerMove)

    #result messages
    if result == 'win':
        print("Hooray!! You win!")
    elif result == 'lose':
        print("So sad.... you lose!")
    else:
        print("It was a draw! Try again!!")
    print("--------------------------------------") #create some space between next play