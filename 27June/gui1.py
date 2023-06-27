import tkinter as tk

def entry1Manipulation():
    entry1.delete(0,tk.END)
    entry1.insert(0,"Here's some text!")

def text1Manipulation():
    text1.delete("0.0",tk.END)
    text1.insert("0.0","Here's some text!")   

#Create window
root = tk.Tk() 

#Set window properties
root.title("My window of awesomeness")
root.geometry("800x300")
root.configure(background="#cb00cb")

#Create a label
label1 = tk.Label(root,text="Hello world!",width=20,height=3,bg="navyblue",fg="white",font=("Arial","16","bold"))
label1.place(x=15,y=15)

label2 = tk.Label(root,text="Another label")
label2.pack()

entry1 = tk.Entry(root,width=20)
entry1.pack()

button1 = tk.Button(root,width=20,height=3,text="Click me!!",command=entry1Manipulation)
button1.pack()

text1 = tk.Text(root,height=2)
text1.pack()

button2 = tk.Button(root,width=20,height=3,text="Clear textbox!!",command=text1Manipulation)
button2.pack()

#Run window loop
root.mainloop()