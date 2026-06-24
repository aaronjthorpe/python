#THis version of the temperature converter asks the user where they want to save temp data.
#Only asks if file is not already selected.

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk   #Pillow  Python Image Library
import os

def update_label():
    celcius = float(my_entry.get())
    farenheit = round((celcius * 1.8) + 32,3)
    #farenheit = (celcius * 1.8) + 32
    message = f"{celcius}°C is {farenheit}°F"
    #my_label.config(text=(celcius *1.8) + 32)
    my_label.config(text=message,background='purple',width=len(message))

    global file_name #file_name is defined in main function as False
    if not file_name: #If it's False, ask for a real file name
        file_name = filedialog.asksaveasfilename(defaultextension=".txt", # default to text file
                                            initialdir='C:/Pythoncode', # default folder
                                            initialfile='test5.txt', # default filename
                                            filetypes =[('Text file','*.txt')]) #limit to only text files.  Filetypes option takes a list of tuples e.g. [(filetype1,extension1), (filetype2,extension2)...]
    with open(file_name,"a") as f:
        message = message.replace("°"," degrees ") # Replace degree symbol with word as plain text can't take symbol
        f.write(f"{message}\n")
    my_entry.delete(0,tk.END)
    my_entry.focus()


root = tk.Tk()
root.geometry("500x300")
root.title("Temperature Converter")
root.config(background="lightskyblue")

global file_name
file_name = False

#Load image and build Tkinter version
image_file = 'image.png'
if os.path.exists(image_file):
    image_data = Image.open(image_file)
    #Can do manipulations on image if desired e.g. resize.
    #kpi_image.resize(100,100)
    image_tk = ImageTk.PhotoImage(image_data)

    #Create a label, and place image on label.
    image_label = tk.Label(master=root,image=image_tk)
    image_label.pack()
else:
    image_label = tk.Label(master=root,text="Image not found")
    image_label.pack()


instructions_label = tk.Label(master=root,text="Type in a temperature in degrees celcius and click the button to display degrees farenheit")
instructions_label.pack()

my_label = tk.Label(master=root
                    ,background='orangered'
                    ,foreground='white'
                    ,width=3
                    ,font=('Arial',10)
                    ,height=2
                    )
my_label.pack()

my_entry = tk.Entry(master=root)
my_entry.focus()
my_entry.pack()

my_button = tk.Button(master=root,text="Convert",command=update_label)
my_button.pack()
quit_button = tk.Button(master=root,text="Quit", command=lambda: root.destroy())
quit_button.pack()

# lambda function
# (inline function) - define and run all in one; no def line.
# useful for one-line or v. simple functions. 




root.mainloop()

print("GUI mainloop complete")