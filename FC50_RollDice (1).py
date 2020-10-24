from tkinter import *
import random


window = Tk()
window.geometry('500x500')
window.title("THE ROLLING DICE GAME")
window.configure(height=120, width=346, background="Teal")
label=Label(window, text=" ", font=("Impact", 19))
def roll():
    dice=["1","2","3","4","5","6"]
    print(random.choice(dice))


button=Button(window, text="Roll Dice", command=roll, padx=23, pady=12, activebackground="pink", font=("Impact", 17), foreground="maroon")
button.pack()

def close_window():
    window.destroy()
    exit()

ext=Button(window, text="EXIT", width=14, command=close_window)
ext.pack()

window.mainloop()
