#gui
# import flashcards
import tkinter as tk
from tkinter import *
import tkinter.simpledialog
from tkinter.simpledialog import *
import os
root = Tk()
def mainpg():
    root.title("Flashcards")
    root.geometry('500x500')
    
    #elements of page one
    head = Label(root, text="Flashcards simulator",font=("Times", 50))
    head.pack()
    root.mainloop()
mainpg()