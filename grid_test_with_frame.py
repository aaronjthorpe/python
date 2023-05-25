import tkinter as tk
from tkinter import ttk  #separator requires ttk

mywindow = tk.Tk()
#mywindow.configure(background='black')

titlelabel = tk.Label(mywindow,text="Title",background='pink',width=75,font=("Arial,20"))
titlelabel.pack()

sep1 = ttk.Separator(mywindow,orient='horizontal')
sep1.pack()

myframe = tk.Frame(bg='gray',height=30,width=75)
myframe.pack()  #frame is packed into Window....

#... then labels are 'gridded' into frame
label1 = tk.Label(myframe,text='label 1',background='yellow',width=20)
label1.grid(column=0,row=0)
label2 = tk.Label(myframe,text='label 2',background='green',width=20)
label2.grid(column=1,row=0)


mywindow.mainloop()