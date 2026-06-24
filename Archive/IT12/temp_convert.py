#import modules
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime

#Convert Temperature Function
def convertTemp(event=None):
    fltTempInput = float(entTempInput.get())

    if strTemperatureScale.get() == "C":
        #Convert to Farenheit
        fltTempOutput = (fltTempInput * 1.8) + 32
        strTempOutput = str(round(fltTempOutput,2)) + "°F"
        #print(fltTempOutput) # for debugging
    elif strTemperatureScale.get() == "F":
        #Convert to Celcius
        fltTempOutput = (fltTempInput - 32) / 1.8
        strTempOutput = str(round(fltTempOutput,2)) + "°C"
        #print(fltTempOutput) # for debugging

    #Update Label
    lblOutput.config(text=strTempOutput) 

    # #Ask for File To Save
    # filename = filedialog.askopenfilename(initialdir="C:\\AaronSeptember\\filesdemo",initialfile="Temperature.txt")

    # #Save data to file
    # with open(filename,"a") as f:
    #     f.write("\n")
    #     f.write(strTemperatureScale.get())
    #     f.write(",")
    #     f.write(entTempInput.get())
    #     f.write(",")
    #     f.write(str(round(fltTempOutput,2)))
    #     f.write(",")
    #     f.write(lblClock.cget("text"))

    #Reset entry box
    #entTempInput.delete(0,tk.END)
    entTempInput.select_range(0,tk.END)
    entTempInput.focus()

#Function to Update 'Clock' Label
def updateDateTime():
    CurrentDateTime = datetime.now()
    FormattedDateTime = CurrentDateTime.strftime("%d/%m/%Y %H:%M:%S")
    lblClock.config(text = FormattedDateTime)
    lblClock.after(1000, updateDateTime)

#Create main window and set properties
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("320x150")
window.configure(background="#efbdfc")

#Configure Grid for Window
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)
window.rowconfigure(4,weight=1)

#Create labels
lblTitle = ttk.Label(window,text="Temperature Converter",font="calibri 24",background="#e99ffc")
lblTitle.grid(column=0,row=0,columnspan=2)

strInstructionText = "\U0001F975\U0000FE0F Enter a temperature, select a scale, and click 'convert'  \U0001F976\U0000FE0F"
#lblInstruction = ttk.Label(window,text="Enter a temperature, select a scale, and click 'convert'",background="#e99ffc")
lblInstruction = ttk.Label(window,text=strInstructionText,background="#e99ffc")
lblInstruction.grid(column=0,row=1,columnspan=2)

lblOutput = ttk.Label(window,text="",background="#efbdfc",foreground="red",font="calibri 12 bold")
lblOutput.grid(column=1,row=3)

#Create 'Clock' label and call function to update
lblClock = ttk.Label(window, text="",background="#efbdfc")
lblClock.grid(column=1,row=4)
updateDateTime()

#Create Entrybox
entTempInput = ttk.Entry(window)
entTempInput.grid(column=0,row=2,sticky="ew",padx=5,pady=5)
entTempInput.bind("<Return>",convertTemp)

#Create Button
btnConvert = ttk.Button(window,text="Convert",command=convertTemp)
btnConvert.grid(column=1,row=2,sticky="ew",padx=5,pady=5)

#Create Radiobuttons
strTemperatureScale = tk.StringVar()
strTemperatureScale.set("C")

optCelcius = tk.Radiobutton(window,text="Celcius",value="C",variable=strTemperatureScale,background="#efbdfc",anchor="w")
optCelcius.grid(column=0,row=3,sticky="ew")

optFarenheit = tk.Radiobutton(window,text="Farenheit",value="F",variable=strTemperatureScale,background="#efbdfc",anchor="w")
optFarenheit.grid(column=0,row=4,sticky="ew")

#Give focus to Entry Box
entTempInput.focus()

#Run TKinter Main Loop
window.mainloop()