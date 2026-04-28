import tkinter as tk

window = tk.Tk()
window.geometry("500x500")
window.title("Pack")

button1 = tk.Button(master=window, text="Button 1")
button2 = tk.Button(master=window, text="Button 2")
button3 = tk.Button(master=window, text="Button 3")
button4 = tk.Button(master=window, text="Button 4")
button5 = tk.Button(master=window, text="Button 5")
button6 = tk.Button(master=window, text="Button 6")
button7 = tk.Button(master=window, text="Button 7")
button8 = tk.Button(master=window, text="Button 8")
button9 = tk.Button(master=window, text="Button 9")

for i in range(1,10):
    globals()['button' + str(i)].pack()

#alternative
button1.pack()
button2.pack()
button3.pack()
button4.pack(anchor="e")
button5.pack()
button6.pack(anchor="center")
button7.pack()
button8.pack()
button9.pack(anchor="w")


window.mainloop()