#Taken from Copilot.  A 'whirlwind tour' of all(?) the tkinter widgets

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser
# ttk = Themed tkinter - 'addon' / newer version with more options thank 'pure' tk. 


def on_button_click():
    messagebox.showinfo("Button Clicked", f"Entry says: {entry.get()}")

def on_check():
    messagebox.showinfo("Checkbox", f"Checkbox value: {check_var.get()}")

def on_radio():
    messagebox.showinfo("Radio", f"Selected: {radio_var.get()}")

def on_scale(val):
    scale_label.config(text=f"Scale Value: {val}")

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        color_label.config(text=f"Selected Color: {color}", bg=color)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        messagebox.showinfo("File Selected", file_path)

def submit_form():
    messagebox.showinfo("Form Submitted", f"Text: {text.get('1.0', tk.END)}")

# Main window
root = tk.Tk()
root.title("Tkinter Widgets Showcase")
root.geometry("600x700")

# Label
label = tk.Label(root, text="This is a Label", font=("Arial", 14))
label.pack(pady=5)

# Entry
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=5)

# Checkbutton
check_var = tk.BooleanVar()
check_btn = tk.Checkbutton(root, text="Check Me", variable=check_var, command=on_check)
check_btn.pack(pady=5)

# Radiobuttons
radio_var = tk.StringVar(value="Option 1")
radio_var_2 = tk.StringVar(value="Option 3")
tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1", command=on_radio).pack()
tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2", command=on_radio).pack()
tk.Radiobutton(root, text="Option 3", variable=radio_var_2, value="Option 3", command=on_radio).pack()
tk.Radiobutton(root, text="Option 4", variable=radio_var_2, value="Option 4", command=on_radio).pack()

# Listbox
listbox = tk.Listbox(root, height=4)
for item in ["Apple", "Banana", "Cherry", "Date"]:
    listbox.insert(tk.END, item)
listbox.pack(pady=5)

# Combobox
combo = ttk.Combobox(root, values=["Python", "Java", "C++"])
combo.current(2)
combo.pack(pady=5)

# Scale
scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=on_scale)
scale.pack(pady=5)
scale_label = tk.Label(root, text="Scale Value: 0")
scale_label.pack()

# Spinbox
spinbox = tk.Spinbox(root, from_=1, to=10)
spinbox.pack(pady=5)

# Text widget
text = tk.Text(root, height=4, width=40)
text.pack(pady=5)

# Canvas
canvas = tk.Canvas(root, width=200, height=100, bg="lightgray")
canvas.create_oval(20, 20, 80, 80, fill="blue")
canvas.create_rectangle(100, 20, 180, 80, fill="red")
canvas.pack(pady=5)

# Menu
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

# Color chooser
color_btn = tk.Button(root, text="Choose Color", command=choose_color)
color_btn.pack(pady=5)
color_label = tk.Label(root, text="No color selected", width=30)
color_label.pack(pady=5)

# Submit button
submit_btn = tk.Button(root, text="Submit Form", command=submit_form)
submit_btn.pack(pady=10)

root.mainloop()
