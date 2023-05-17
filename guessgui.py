"""
Dodgy Guessing Game with GUI
guessgui.py
Aaron Thorpe
17/5/2023
aaron.thorpe@academyit.com.au

This game will pick a number between 1 and 100, and then ask the user
to guess the number.  Users will enter their guess in an entrybox and
can either press Enter or click the Check Guess button to see if they
win.  The app should tell the user if their guess is too small or too
big and keep track of how many gueses they have made.

Users can reset the game by clicking the reset button, or use the
menu to reset or quit.
"""
#import modules.  Messagebox is ued to ask for confirmation of quit or reset
import tkinter as tk
import tkinter.messagebox as mb
from random import randint

#Generate random number and initialise number of guesses
randomNumber = randint(1,100)
guesses = 0

#function for resetting game
def reset():
    answer = mb.askyesno("Reset?","Are you sure you want to reset?")
    if answer == True:
        global randomNumber
        randomNumber = randint(1,10) #generate new random number
        global guesses
        guesses = 0

        #reset UI
        lbltitle.config(text="I am thinking of a number between 1 and 10")
        mywindow.configure(background="#123456")
        entuserguess.delete(0, tk.END)
        lblguesses.config(text="Guesses: " + str(guesses))

    #Set focus on entry box    
    entuserguess.focus()

#function to confirm quit action and quit program if yes.
def quityesno():
    answer = mb.askyesno("Quit?","Are you sure you want to quit?")
    if answer == True:
        mywindow.destroy()

#function to trigger check of guess if user presses Enter ('return') on entrybox
def return_pressed(event):
    checkguess()

#core logic of game.  Is the guess correct, higher, or lower?
def checkguess():
    global guesses
    guesses += 1
    lblguesses.config(text="Guesses: " + str(guesses))
    userentry = int(entuserguess.get())

    if userentry == randomNumber:
        lbltitle.config(text="Congrats you got it right in " + str(guesses) + " guesses!")
        mywindow.config(bg="green")
    elif userentry < randomNumber:
        lbltitle.config(text="WRONG!  Your guess is lower than my number.")
        mywindow.config(bg="yellow")
    else:
        lbltitle.config(text="WRONG!  Your guess is higher than my number.")
        mywindow.config(bg="orange")

#create window
mywindow = tk.Tk()

#window settings
mywindow.title("Aaron's amazing app is awesome")
mywindow.geometry("800x160")
mywindow.configure(background="#123456")

#create label
lbltitle = tk.Label(
    mywindow, 
    text="I am thinking of a number between 1 and 10", 
    width=40, height=2,
    bg="deepskyblue",
    fg="white",
    font=("Arial","16","bold"))
lbltitle.pack()

#create entry box
entuserguess = tk.Entry(mywindow,width=40)
entuserguess.bind('<Return>',return_pressed)  #call return_pressed function if Enter/Return is pressed
entuserguess.focus()
entuserguess.pack()

#create check guess button
btncheckguess = tk.Button(
    mywindow, text="Check guess", width=40, height=2, 
    bg="navyblue",fg="white",command=checkguess #call checkguess function when clicked
    )
btncheckguess.pack()

#create reset button
btnreset = tk.Button(
    mywindow, text="Reset", width=40, height=2, 
    bg="navyblue",fg="white",command=reset #call reset function when clicked
    )
btnreset.pack()

#create image, and label to place image
imgicon = tk.PhotoImage(file='question-mark.png')
lblimgicon = tk.Label(image=imgicon)
lblimgicon.place(x=10,y=10,anchor="nw")

#create label for number of guesses
lblguesses = tk.Label(text="Guesses: " + str(guesses),bg="deepskyblue",fg="white",font=("arial","12"))
lblguesses.place(x=700,y=10)

#create menubar and associate with window
menubar = tk.Menu(mywindow)
mywindow.config(menu=menubar)

#create file menu and associate with menu bar
file_menu= tk.Menu(menubar)
file_menu.add_command(label='Reset',command=reset) #call reset function
file_menu.add_separator()
file_menu.add_command(label='Exit',command=quityesno) #call quit function

#add file menu to menu bar
menubar.add_cascade(label="File",menu=file_menu)

#run GUI
mywindow.mainloop()