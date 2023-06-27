import random
import tkinter as tk

def rolldice():
    global label
    result = random.randint(1,6)
    
    if result == 1:
        dicefile = "dice_images\dice_1.png"
        dice = tk.PhotoImage(file=dicefile)
        label.config(image=dice)
        label.photo(dice)

        
    elif result == 2:
        dicefile = "dice_images\dice_2.png"
        dice = tk.PhotoImage(file=dicefile)
        label.config(image=dice)
        label.photo(dice)

    elif result == 3:
        dicefile = "dice_images\dice_3.png"
        dice = tk.PhotoImage(file=dicefile)
        label.config(image=dice)
        label.photo(dice)

    elif result == 4:
        dicefile = "dice_images\dice_4.png"
        dice = tk.PhotoImage(file=dicefile)
        label.config(image=dice)
        label.photo(dice)

    elif result == 5:
        dicefile = "dice_images\dice_5.png"
        dice = tk.PhotoImage(file=dicefile)
        label.config(image=dice)
        label.photo(dice)

    elif result == 6:
        dicefile = "dice_images\dice_6.png"
        dice = tk.PhotoImage(file=dicefile)
        label.config(image=dice)
        label.photo(dice)

def main():

    global label
    global dice

    window = tk.Tk()
    window.title("Roll the dice")
    window.configure(background="darkred")
    window.geometry('200x200')

    button = tk.Button(window,text="Roll!",command=rolldice)
    button.pack()

    label = tk.Label(window)
    label.pack()
    
    window.mainloop()

if __name__ == '__main__':
    main()