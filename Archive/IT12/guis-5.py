# Shows most of the differnt options for messagebox.
# Takes result of message box selection and displays on label.
# Note how some produce 1 or 0, but some are Yes/No
import tkinter as tk
from tkinter import messagebox

def ok_cancel():
    result = messagebox.askokcancel("Message Box", "Okay or cancel?")
    label.config(text=result)
    pass

def ask_question():
    result = messagebox.askquestion("Message Box","Question?")
    label.config(text=result)

def ask_yes_no():
    result = messagebox.askyesno("Message Box","Yes or no?")
    label.config(text=result)

def ask_retry_cancel():
    result = messagebox.askretrycancel("Message Box","Retry or cancel?")
    label.config(text=result)

def show_error():
    result = messagebox.showerror("Message Box","This is an error")
    label.config(text=result)

def show_warning():
    result = messagebox.showwarning("Message Box","This is a warning")
    label.config(text=result)

def show_info():
    result = messagebox.showinfo("Message Box","This is information.")
    label.config(text=result)

root = tk.Tk()
root.title("All the message boxes")
root.config(background='#000000')

button1 = tk.Button(master=root, text="OK/Cancel",command=ok_cancel).pack(pady=5)
button2 = tk.Button(master=root, text="Question",command=ask_question).pack(pady=5)
button3 = tk.Button(master=root, text="Yes/No",command=ask_yes_no).pack(pady=5)
button4 = tk.Button(master=root, text="Retry/Cancel",command=ask_retry_cancel).pack(pady=5)
button5 = tk.Button(master=root, text="Error",command=show_error).pack(pady=5)
button6 = tk.Button(master=root, text="Warning",command=show_warning).pack(pady=5)
button7 = tk.Button(master=root, text="Info",command=show_info).pack(pady=5)

label = tk.Label(master=root,text="",width=30,height=2)
label.pack()

root.mainloop()