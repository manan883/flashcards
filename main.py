#gui
# import flashcards
from email import message
from genericpath import exists
from ssl import Options
import tkinter as tk
from tkinter import *
from tkinter import dialog
import tkinter.simpledialog
from tkinter.simpledialog import *
import os
import sys 
from turtle import title
import random
root = Tk()
universalD = {'\**/': []
}

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
def addQuestions(name):
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
                        aw = tkinter.simpledialog.askstring(title="Flashcards",prompt="Enter the answer to the question:\n" + qt)
                        if aw == "" or None:
                            tkinter.messagebox.showerror(title="Flashcards",message="Answer can not be empty")
                        if aw != "" or None:
                            newSetDic["answers"].append(aw)
                case "B":
                    writeToFile(name,newSetDic)
                    break
def deleteSet(name):
    try:
        fn = name + "_data.txt"
        os.remove(fn)
    except:
        tkinter.messagebox.showinfo(message="File does not exist")
def newSet():
        name = tkinter.simpledialog.askstring(title="Flashcards",prompt="Enter the name of the new set: ",parent=root)
        fn = name + "_data.txt"
        if exists(fn):
            dat = False
            dat = tkinter.messagebox.askyesno(title="Flashcards",message="Set already exists: do you want to replace it? ")
            if dat == False:
                tkinter.messagebox.showinfo(title="Flashcards",message="The new data will be added to the set")
                addQuestions(name)
            else:
                deleteSet(name)
                addQuestions(name)
        else:
            addQuestions(name)
def appendO():
        name = tkinter.simpledialog.askstring(title="Append",prompt="Enter the name of the set you want to append to")
        fn = name + "_data.txt"
        if not(exists(fn)):
            val = tkinter.messagebox.askyesno(message="Set does not exist, do you want to make a new one?")
            if val == True:
                addQuestions(name)
        elif exists(fn):
            f = open(fn,"a")
            addQuestions(name)
def studySet():
    name = tkinter.simpledialog.askstring(title="",prompt="Enter the name of the set you want to study")
    try:
        fn = name + "_data.txt"
        f = open(fn,"r")
        arr = []
        for x in f:
            arr.append(x)
        
        for i in arr:
            temp = i.split(",")
            universalD[temp[0]] = temp[1]
        random.shuffle(arr)
        print("The questions will show up one at a time, press Q at any time to quit")
        tkinter.messagebox.showinfo(title="Flashcards",message="The questions will show up one at a time")
        for i in arr:
            temp = i.split(",")
            #do a continue to answer with the one button 
            quet = tkinter.messagebox.showinfo(title="",message=("Question\n" + temp[0] + "\nPress Ok to view the answer"))
            if quet == "ok":
                m = universalD[temp[0]] + "\nContinue?"
                yesno = tkinter.messagebox.askyesno(title="",message=m)
            
            #do a yes no and on the bottom ask the user to continue 
            # yesno = tkinter.messagebox.askyesno(title="Questions",message=("Question\n" + temp[0] + "\nDo you wish to continue"))
            if yesno == False:
                break
            # m = universalD[temp[0]]
            # tkinter.messagebox.showinfo(title="",message=m)
            # print("The answer to:",temp[0],"is",universalD[temp[0]])
        else:
            tkinter.messagebox.showinfo(title="",message="Set complete")
    except:
        print("Set does not exist, would you like to make a new set with this name? Y/N ")
        usi = input()
        match usi.upper():
            case "Y":
                newSet(name)
            case "N":
                return
            case _:
                print("Type Y or N")
        


def pg2():
    root.withdraw()
    option = tk.Tk()
    option.title("Flashcards")
    nS = Button(option,text="Make a new set",font=("Times",15),command=newSet)
    nS.grid(row = 1,column= 1)
    aO = Button(option,text="Append to an old set",font=("Times",15),command=appendO)
    aO.grid(row = 2, column= 2)
    stdy = Button(option,text="Study a set",font=("Times",15),command=studySet)
    stdy.grid(row = 3, column= 1)
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