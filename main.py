#gui
# import flashcards
from email import message
import tkinter as tk
from tkinter import *
import tkinter.simpledialog
from tkinter.simpledialog import *
import os
from turtle import title
root = Tk()


def writeToFile(name,dataDict):
    fn = str(name + "_data.txt")
    try:
        
        f = open(fn,"x")
    except:
        pass
    ap = open(fn,"a")
    for i,j in zip(dataDict["questions"], dataDict["answers"]):
        ap.write(i + "," + j + "\n")
        #print(i + "," + j)
    pass
def newSet():
    name = tkinter.simpledialog.askstring(title="Flashcards",prompt="Enter the name of the new set: ",parent=root)
    newSetDic = {
        "questions": [],
        "answers": []
    }
    while True:
        ipt = tkinter.simpledialog.askstring(title="Flashcards",prompt="A: Enter a question you want to add to the library:\nB: quit",parent=root)
        match ipt.upper():
            case "A":
                qt = ""
                while qt == "" or None:                    
                    qt = tkinter.simpledialog.askstring(title="Flashcards",prompt="Enter the question",parent=root)
                    if qt == "" or None:
                        tkinter.messagebox.showerror(title="Flashcards",message="Question can not be empty")
                    if qt != "" or None:
                        newSetDic["questions"].append(qt)
                aw = ""
                while aw == "" or None:               
                    aw = tkinter.simpledialog.askstring(title="Flashcards",prompt="Enter the answer to the question")
                    if aw == "" or None:
                        tkinter.messagebox.showerror(title="Flashcards",message="Answer can not be empty")
                    if aw != "" or None:
                        newSetDic["answers"].append(aw)
            case "B":
                writeToFile(name,newSetDic)
                break
def pg2():
    root.withdraw()
    options = tk.Tk()
    options.title("Flashcards")
    nS = Button(options,text="Make a new set",font=("Times",15),command=newSet)
    nS.grid(row = 1,column= 1)
def mainpg():
    root.title("Flashcards")
    root.geometry('500x500')
    
    #elements of page one
    head = Label(root, text="Flashcards simulator",font=("Times", 50))
    head.pack()
    explain = Label(root,text="This can add flashcards to a set and allow you to study them one by one",wraplength=300,font=("Times",25))
    explain.place(relx=0.5,rely=0.5,anchor=CENTER)
    enter = Button(root,text="Enter application",font=("Times",15),fg='grey',command=pg2)
    enter.place(relx=0.5,rely=0.8,anchor=CENTER)
    root.mainloop()
mainpg()