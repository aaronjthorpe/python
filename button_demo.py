import tkinter as tk

#Function that will run when button is clicked
#function puts text into label
def DoThings():
    mylabel.config(text="Some text!!!")

#Define window
mywindow = tk.Tk()

#Create label.  Label is empty/blank when program first runs
mylabel = tk.Label(mywindow,text="")
mylabel.pack()

#Create button.  Button will run the function DoThings defined above.
mybutton = tk.Button(mywindow,text="Click me!!",command=DoThings)
mybutton.pack()




mywindow.mainloop()

