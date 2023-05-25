import tkinter as tk

#create window
mywindow = tk.Tk()


#title label spans two columns
labeltitle = tk.Label(mywindow, text="TITLE",bg='yellow',width=100) #note width is double other labels
labeltitle.grid(column=0,row=0,columnspan=2)  #columnspan = 2  makes the column two columns wide

#create four other labels in 'square' pattern (2 x 2)
label1 = tk.Label(mywindow, text="Label1",bg='navyblue',width=50)
label1.grid(column=0,row=1)
label2 = tk.Label(mywindow, text="Label2",bg='blue',width=50)
label2.grid(column=1,row=1)
label3 = tk.Label(mywindow, text="Label3",bg='lightblue',width=50)
label3.grid(column=0,row=2)
label4 = tk.Label(mywindow, text="Label4",bg='royalblue',width=50)
label4.grid(column=1,row=2)

mywindow.mainloop()