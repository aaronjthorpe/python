#Graphical User Interface (GUI)

# We are using tkinter.  Tk = Graphical framework 
# included in the Python Standard Library
# https://docs.python.org/3/library/tkinter.html

# tkinter makes use of
# Object-oriented Programming (OOP)

import tkinter as tk

root = tk.Tk()  # create a new object of class Tk.  Tk class is our 'app' and also our first window.
root.geometry(("500x500"))  # set window size (horizontal pixels x vertical pixels)
root.title("Anything you like in here")  # window title
#root.configure(bg="thistle")  # background colour. named colour or 6 hexadecimal digits 0 - F
root.configure(bg='#123ABC') 

#If using grid geometry manager, configure columns and rows
root.columnconfigure(0) #, minsize=300)
root.columnconfigure(1) #, minsize=100)
root.columnconfigure(2) #, minsize=100)
#root.rowconfigure

#Create a bunch of Label objects. Set master to root (they live on root window), set text, some other options for some labels.
message_label0 = tk.Label(master=root,text="Title Label!!!")
message_label1 = tk.Label(master=root,text="Hello, world 1",background='blue',foreground='red',font=('Comic Sans MS',40,'bold'))
message_label2 = tk.Label(master=root,text="Hello, world 2",padx=25,pady=25)
message_label3 = tk.Label(master=root,text="Hello, world 3")
message_label4 = tk.Label(master=root,text="Hello, world 4")
message_label5 = tk.Label(master=root,text="Hello, world 5")
message_label6 = tk.Label(master=root,text="Hello, world 6")
message_label7 = tk.Label(master=root,text="Hello, world 7")
message_label8 = tk.Label(master=root,text="Hello, world 8")
message_label9 = tk.Label(master=root,text="Hello, world 9")

message_label7.config(text="I changed the text.") # Config can be changed after definition.  MANY options.

# #geometry manager - pack.  Pack puts items by default as close to top as possible.  anchor can overwrite.
message_label1.pack()
message_label2.pack(anchor='center')
message_label3.pack(anchor='sw')
message_label4.pack(anchor='s')
message_label5.pack()
message_label6.pack()
message_label7.pack()
message_label8.pack()
message_label9.pack()

# #geometry manager - place.  Place allows the user to set custom x and y coordinates for widgets.
message_label1.place(x=100,y=100)
message_label2.place(x = 100,y=200)
message_label3.place(x=100,y=300)
message_label4.place(x=100,y=400)
message_label5.place(x=100,y=0)

# Geometry manager - grid.  Grid will put widgets on columns and rows, starting with 0.
# message_label0.grid(column=0,row=0,columnspan=3)
# message_label1.grid(column=0,row=1)
# message_label2.grid(column=0,row=2)
# message_label3.grid(column=0,row=3)
# message_label4.grid(column=1,row=1)
# message_label5.grid(column=1,row=2)
# message_label6.grid(column=1,row=3)
# message_label7.grid(column=2,row=1)
# message_label8.grid(column=2,row=2)
# message_label9.grid(column=2,row=3)

root.mainloop() # this line will always be at the bottom.  It runs the GUI and listens for events.





