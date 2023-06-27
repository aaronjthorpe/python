#Import Modules
import tkinter as tk
import tkinter.messagebox as mb
from random import randint

#Start Game
#Generate Random Number between 1 and 100
# and Initialise Number of Guesses

randomNumber = randint(1,100)
guesses = 0

#Define functions

#Check user's guess against random number.
def checkGuess():
    global guesses
    global randomNumber

    #increment guess count and update count label
    guesses += 1
    numberGuesses.config(text="Guesses: " + str(guesses))

    #Retrieve user guess from entrybox and convert to int
    userGuessValue = int(userGuess.get())

    #Game logic
    if userGuessValue == randomNumber:
        title.config(text = "Woohoo!! You won in " + str(guesses) + " guesses!")
        root.config(background="green")
    elif userGuessValue < randomNumber:
        title.config(text="Nope.  Choose a higher number!")
        root.config(background="yellow")
    else:
        title.config(text="WRONG! Choose a lower number!")
        root.config(background="orange")

#Reset game to beginning
def reset():
    global randomNumber
    global guesses

    #Ask user for confirmation before reset
    answer = mb.askyesno("Reset??","Are you sure you want to reset the game?")

    if answer == True: #user clicked yes in messagebox

        #Reset the number of guesses and the random number
        randomNumber = randint(1,100)
        guesses = 0

        #Reset the user interface
        title.config(text="I am thinking of a number between 1 and 100.")
        root.configure(background="#123456")
        userGuess.delete(0,tk.END)
        userGuess.focus()
        numberGuesses.config(text="Guesses: " + str(guesses))

#When enter/"return" is pressed while guess entrybox is in focus
#Run the check guess function
def return_pressed(event):
    checkGuess()

#This function runs when the user clicks Exit in the file menu
def endGame():
    #ask for confirmation
    answer = mb.askyesno("Quit???","Do you want to quit the game?")

    if answer == True:
        root.destroy()   #exit application 



#Create Window
root = tk.Tk()

#Window Settings
root.title("Guessing game")
root.geometry("800x160")
root.configure(background="#123456")

#Create title label and pack
title = tk.Label(
    root,
    text="I am thinking of a number between 1 and 100",
    width=40,
    height=2,
    background="deepskyblue",
    foreground="white",
    font=("Arial",16,"bold")
    )
title.pack()

#Create guess entrybox and pack
userGuess = tk.Entry(root,width=40)
userGuess.focus()
userGuess.bind('<Return>',return_pressed)
userGuess.pack()

#Create check guess button and pack
checkGuessButton = tk.Button(root,text="Check guess",command=checkGuess, width=40, height=2)
checkGuessButton.pack()

#Create reset button and pack
resetButton = tk.Button(root,text="Reset",width=40,height=2,command=reset)
resetButton.pack()

#Create label for graphic and place
icon = tk.PhotoImage(file="question-mark.png")
iconlabel = tk.Label(image=icon,background="#123456")
iconlabel.place(x=10,y=10,anchor="nw")

#Create label for guess count and place
numberGuesses = tk.Label(text="Guesses: " + str(guesses),  
                         background="deepskyblue",
                         foreground="white",
                         font=("Arial","12"))
numberGuesses.place(x=700,y=10)

#Create menubar and configure window with menubar
menubar = tk.Menu(root)
root.config(menu=menubar)

#Create file menu and add commands
file_menu = tk.Menu(menubar)
file_menu.add_command(label="Reset",command=reset)
file_menu.add_command(label="Exit",command=endGame)

#Add file menu to menubar
menubar.add_cascade(label="File",menu=file_menu)

#Run Mainloop
root.mainloop()

