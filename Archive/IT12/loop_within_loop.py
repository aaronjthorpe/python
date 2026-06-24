game = 1
while game == 1:
    print("Begin the game.")
    guess = 0
    while True:
        try:
            guess = input("Guess a number: ")
            if guess == 'x':
                break
            guess = int(guess)
            print(f"Your guess was {guess}")
            
        except:
            print("Type a valid number.")
    #if guess == 'x':
        #break
    print("Ending the game")
    game = 0
