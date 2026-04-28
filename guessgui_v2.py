docstring = """
Dodgy Guessing Game with GUI
guessgui_v2.py

Aaron Thorpe
Version 1.0 17/5/2023
Version 2.0 28/4/2026
aaron.thorpe@academyit.com.au

This game will pick a 'random' number between 1 and 10, and then ask 
the user to guess the number.  Users will enter their guess in an entrybox
and can either press Enter or click the Check Guess button to see if they
win.  The app should tell the user if their guess is too small or too big and 
keep track of how many gueses they have made; their score.

Users can reset the game by clicking the reset button, or use the
menu to reset or quit.

Version 2 Update Notes:
-Added error handling for non-int entry values
-Added logic to check if guess was above maximum or below minimum of random range i.e. invalid guess.  
    - Don't count this as a guess.
-Fixed question mark png transparency
-Tweaked guess count label layout
-Add y-axis padding to pack objects
-Various visual adjustments
-Adjusted enter-press function to highlight and focus entry box for easier new guess entry
-Add keyboard bindings for Ctrl-r to reset, Ctrl-q to quit. F1 for help. 
-Had to add event arguments to those functions as required by key binding, default value of None.
-Add Help window with Text box and button.
"""
#import modules.  Messagebox is ued to ask for confirmation of quit or reset
import tkinter as tk
import tkinter.messagebox as mb
from random import randint

#Generate random number and initialise number of guesses
max_number = 10
min_number = 1
randomNumber = randint(min_number,max_number)
guesses = 0

#function for resetting game
def reset(event = None):
    answer = mb.askyesno("Reset?","Are you sure you want to reset?")
    if answer == True:
        global randomNumber, max_number, min_number
        randomNumber = randint(min_number,max_number) #generate new random number
        global guesses
        guesses = 0

        #reset UI
        lbltitle.config(text="I am thinking of a number between 1 and 10")
        mywindow.configure(background="#123456")
        lblimgicon.config(bg="#123456")
        entuserguess.delete(0, tk.END)
        lblguesses.config(text="Guesses:\n" + str(guesses))

        #Print event if present (debugging)
        #if event:
        #    print(f"Resetting due to: {event}")

    #Set focus on entry box    
    entuserguess.focus()

#function to confirm quit action and quit program if yes.
def quityesno(event=None):
    answer = mb.askyesno("Quit?","Are you sure you want to quit?")
    #if answer == True:
    if answer:
        #Print event if present (debugging)
        if event:
            print(f"Quitting due to: {event}")
            mywindow.destroy()
        else:
            mywindow.destroy()


#function to trigger check of guess if user presses Enter ('return') on entrybox
def return_pressed(event):
    checkguess()
    entuserguess.select_range(0,tk.END)
    entuserguess.focus()



#core logic of game.  Is the guess correct, invalid, higher, or lower?
def checkguess():
    global guesses
    try:
        userentry = int(entuserguess.get())
        guesses += 1
        lblguesses.config(text="Guesses:\n" + str(guesses))

        if userentry == randomNumber:
            lbltitle.config(text=f"Congrats you got it right in {guesses} guesses!")
            mywindow.config(bg="green")
            lblimgicon.config(bg="green")
        elif userentry < min_number or userentry > max_number:
            mb.showwarning("Invalid Guess",f"Your guess was out of range.  Please guess a number between {min_number} and {max_number}.")
            guesses -= 1  # Guess doesn't count if it's not valid, right???
            lblguesses.config(text="Guesses:\n" + str(guesses))
        elif userentry < randomNumber:
            lbltitle.config(text="WRONG!  Your guess is lower than my number.")
            mywindow.config(bg="yellow")
            lblimgicon.config(bg="yellow")
        elif userentry > randomNumber:
            lbltitle.config(text="WRONG!  Your guess is higher than my number.")
            mywindow.config(bg="orange")
            lblimgicon.config(bg="orange")
    except ValueError:
        mb.showerror("Invalid guess.","Please enter a valid guess.")

def display_help(event = None):
    help_window = tk.Toplevel(master=mywindow)
    help_window.geometry("700x650")
    help_window.resizable(width=False,height=False)
    help_window.title("About Guessing Game")
    help_window.config(background="#aaaaaa")
    help_textbox = tk.Text(master=help_window,wrap="word",height=34)
    #help_textbox.insert(tk.END,f"The guessing game is a lame python app built by Aaron Thorpe in 2023 and refinded in 2026.\nIt's goal is primarily to demonstrate tkinter features.\nPlayers must guess a number between {min_number} and {max_number}.\nThe game will tally their guesses.\nPlayers can reset the game by clicking Reset or pressing Control+R.\n")
    help_textbox.insert(tk.END,docstring) # decided to just put docstring in help window rather than new text.
    help_textbox.config(state=tk.DISABLED) # make text box readonly
    help_textbox.pack(padx=10,pady=20)
    help_close_button = tk.Button(master=help_window, text='Great!',command=lambda: help_window.destroy())
    help_close_button.pack(pady=(10,0))
    


#create window
mywindow = tk.Tk()

#window settings
mywindow.title("Guessing Game")
mywindow.geometry("800x250")
mywindow.configure(background="#123456")

#adjust window icon
mywindow.iconphoto(True, tk.PhotoImage(file="question-mark.png"))

#bindings
mywindow.bind_all('<Control-r>',reset)
mywindow.bind_all('<Control-q>',quityesno)
mywindow.bind_all('<F1>',display_help)

#create label
lbltitle = tk.Label(
    mywindow, 
    text="I am thinking of a number between 1 and 10", 
    width=40, height=2,
    bg="deepskyblue",
    fg="white",
    font=("Arial",16,"bold"))
lbltitle.pack(pady=(20,10)) # pad 20 above and 10 below

#create entry box
entuserguess = tk.Entry(mywindow,width=40,justify="center",font=("Arial", 14))
entuserguess.bind('<Return>',return_pressed)  #call return_pressed function if Enter/Return is pressed
entuserguess.focus()
entuserguess.pack(pady=10)

#create check guess button
btncheckguess = tk.Button(
    mywindow, text="Check guess", width=30, height=2, 
    bg="teal",fg="white",command=checkguess #call checkguess function when clicked
    )
btncheckguess.pack(side=tk.LEFT,padx=(180,0),pady=10)

#create reset button
btnreset = tk.Button(
    mywindow, text="Reset", width=30, height=2, 
    bg="darkred",fg="white",command=reset #call reset function when clicked
    )
btnreset.pack(side=tk.RIGHT,padx=(0,180),pady=10)

#create image, and label to place image
imgicon = tk.PhotoImage(file='question-mark.png')
lblimgicon = tk.Label(image=imgicon, bg='#123456')
lblimgicon.place(x=20,y=20)

#create label for number of guesses
lblguesses = tk.Label(text="Guesses:\n" + str(guesses),bg="deepskyblue",fg="white",font=("Arial",12),height=3)
lblguesses.place(x=700,y=20)

#create menubar and associate with window
menubar = tk.Menu(mywindow)
mywindow.config(menu=menubar)

#create file, action, help menus and associate with menu bar
file_menu= tk.Menu(menubar,tearoff=False)
file_menu.add_command(label='Reset',command=reset) #call reset function
file_menu.add_separator()
file_menu.add_command(label='Exit',command=quityesno) #call quit function

action_menu = tk.Menu(menubar,tearoff=False)
action_menu.add_command(label='Check Guess',command=checkguess)

help_menu = tk.Menu(menubar,tearoff=False)
help_menu.add_command(label="About",command=display_help)

#add to menu bar
menubar.add_cascade(label="File",menu=file_menu)
menubar.add_cascade(label="Action",menu=action_menu)
menubar.add_cascade(label="Help",menu=help_menu)



#run GUI
mywindow.mainloop()