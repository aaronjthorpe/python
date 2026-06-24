#This 'app' has an image Label, a text Label, an Entry, two buttons.
#It will take data typed into the Entry and put it in the label. 

import tkinter as tk
from PIL import Image, ImageTk   #Pillow  Python Image Library
import os

def update_label():
    message = my_entry.get()  # get method retrieves text from Entry box -> string
    my_label.config(text=message,background='purple',width=len(message)) # Set label to contain text
    my_entry.delete(0,tk.END) # clear entry box contents from position 0 (beginning) to END
    my_entry.focus() # give entry box focus (put cursor in box)


root = tk.Tk()
root.geometry("300x300")
root.config(background="lightskyblue")

#Load image if file present
image_file = 'kpi.png'
if os.path.exists(image_file):
    kpi_image = Image.open(image_file)
    #Can do manipulations on image if desired e.g. resize.
    #kpi_image.resize(100,100)
    kpi_image_tk = ImageTk.PhotoImage(kpi_image) # build Tkinter version of image (ImageTk)

    #Create a label, and place image on label.
    image_label = tk.Label(master=root,image=kpi_image_tk)
    image_label.pack()
else: # if image file not found, put a placeholder
    image_label = tk.Label(master=root,text="Image not found")
    image_label.pack()


my_label = tk.Label(master=root
                    ,background='orangered'
                    ,foreground='white'
                    ,width=3
                    ,font=('Arial',10)
                    ,height=2
                    ) # can spread options over multiple lines if desired.  Personal preference -> clarity
my_label.pack()

my_entry = tk.Entry(master=root)
my_entry.focus()
my_entry.pack()

my_button = tk.Button(master=root,text="Click me!",command=update_label) #runs update_label function when button is clicked.  Note lack of () because that would run function immediately and take the result as the setting for command=.
my_button.pack()
quit_button = tk.Button(master=root,text="Quit", command=lambda: root.destroy())
quit_button.pack()

# lambda function
# (inline function) - define and run all in one; no def line.
# useful for one-line or v. simple functions. 




root.mainloop()

print("GUI mainloop complete") # This will run only after the GUI is closed.