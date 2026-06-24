import tkinter as tk
from PIL import Image, ImageTk   #Pillow  Python Image Library
import os

def update_label():
    if radio_var.get() == 'F': # convert from C to F
        celcius = float(my_entry.get())
        #farenheit = round((celcius * 1.8) + 32,3)  # Optional can round to e.g. 3 decimal places
        farenheit = (celcius * 1.8) + 32
        message = f"{celcius}°C is {farenheit}°F"
    elif radio_var.get() == 'C': # convert from F to C
        farenheit = float(my_entry.get())
        celcius = (farenheit - 32) / 1.8
        message = f"{farenheit}°F is {celcius}°C"
    else:
        message = "Error"

    my_label.config(text=message,background='purple',width=len(message))
    my_entry.delete(0,tk.END)
    my_entry.focus()


root = tk.Tk()
root.geometry("500x300")
root.title("Temperature Converter")
root.config(background="lightskyblue")

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

#tk StringVar can store a variable to be used by widgets.  In this case, currently selected Radio Button value
radio_var = tk.StringVar(value="F")
radio_celcius = tk.Radiobutton(master=root, text="Convert to Celcius", variable=radio_var, value="C")
radio_celcius.pack()
radio_farenheit = tk.Radiobutton(master=root, text="Convert to Farenheit", variable=radio_var, value="F")
radio_farenheit.pack()

my_button = tk.Button(master=root,text="Convert",command=update_label)
my_button.pack()
quit_button = tk.Button(master=root,text="Quit", command=lambda: root.destroy())
quit_button.pack()

# lambda function
# (inline function) - define and run all in one; no def line.
# useful for one-line or v. simple functions. 




root.mainloop()

print("GUI mainloop complete")