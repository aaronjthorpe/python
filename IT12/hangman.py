import random
import time

#Variable initialisation (Creating variables with empty or default vaules)
fruits = ['mango', 'apple', 'banana', 'apricot', 'pineapple', 'cantalope', 'grapefruit', 'jackfruit', 'papaya']
superHeroes = ['hawkeye', 'robin', 'batman', 'galactus', 'thor', 'mystique', 'superman', 'deadpool', 'vision', 'sandman', 'aquaman']

userGuesslist = [] 
userGuesses = [] 
playGame = True 
category = ""  # empty string 
continueGame = "Y"

name = input("Enter your name:   ")
#print("Hello", name.capitalize(), "let's start playing Hangman!")
print(f"Hello {name.capitalize()}.  Let's start playing Hangman!")

time.sleep(0.3)
print("The objective of the game is to guess the secret word chosen by the computer.")
time.sleep(0.3)
print("You can guess only one letter at a time.  Don't forget to press 'enter key' after each guess.")
time.sleep(0.3)
print("Let the fun begin!")
time.sleep(0.3)

while True:
    #Checking the category from which to select the secret word.
    while True:
        if category.upper() == 'X':
            print("Bye, see you next time")
            playGame = False    
            break   #  (or quit())
        elif category.upper() == 'S':
            secretWord = random.choice(superHeroes)
            break
        elif category.upper() == 'F':
            secretWord = random.choice(fruits)
            break     
        else:
            category = input("Please select a valid category:\nF for Fruits\nS for Super-Heros\nX to exit\n")

    if playGame:
        #Break word out into individual characters and store in list
        secretWordList = list(secretWord)
        
        #Decide how many guesses the player can have
        #attempts = len(secretWord) + 2   # Length of word plus 2
        attempts = 6

        # Display 'placeholder'
        def printGuessedLetter():
            print("Your secret word is " + ''.join(userGuesslist))
            time.sleep(2)

        # Calculate number of _ needed and add to list
        for n in secretWordList:
            userGuesslist.append('_ ')

        # Display Placeholder
        printGuessedLetter()

        #print("The number of allowed guesses for this word is: ", str(attempts))
        print(f"You can have {str(attempts)} guesses to find this word.")

        #Actually play the damned game
        while True:
            #print("Guess a letter: ")
            #letter = input()
            letter = input("Guess a letter:\n")

            if letter.upper() in userGuesslist:
                print("You've already guessed that letter.  Try something else.")
            else:
                #attempts -= 1
                userGuesses.append(letter)

                # Correct guess - the letter was in the word.
                if letter in secretWordList:
                    print("Nice guess!")
                    time.sleep(0.3)

                    if attempts > 0:
                        print(f"You have {attempts} attempts left.")

                    #Okay, you're correct, but where in the answer is
                    #your guess.
                    for i in range(len(secretWordList)):
                        if letter == secretWordList[i]:
                            userGuesslist[i] = letter.upper()
                    
                    printGuessedLetter()
                
                #You weren't correct; guess is not in answer
                else:
                    print("WRONG!!!  Try again!")
                    attempts -= 1
                    if attempts > 0:
                        print(f"You have {attempts} attempts left.")
                    printGuessedLetter()

            #Convert guess list back into string, then compare with answer
            joinedList = ''.join(userGuesslist)
            if joinedList.upper() == secretWord.upper():
                print("Yay! You won.")
                time.sleep(2)
                break

            if attempts == 0:
                print("Too many guesses! YOU LOSE!")
                print(f"The secret word that you totally didn't get was {secretWord.capitalize()}")
                break

        continueGame = input("Do you want to play again?\n \
        Y to continue, any other key to quit.\n")
        if continueGame.upper() == "Y":
            # Reset everything so that we're starting fresh next time.
            print("Starting new game....")  # trouble????
            category = input("Please select a valid category:\nF for Fruits\nS for Super-Heros\nX to exit\n")
            userGuesslist = []
            userGuesses = []
            playGame = True
        
        else:
            break
    else:
        break


                    



        



