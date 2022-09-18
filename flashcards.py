from sys import exit
from os import getcwd
from os import path
from os import makedirs
import random
'''
ask user to enter question and answer
put in a map
store question and answer in a csv file with a , as a seperator 
when quizzing user the comma as a parse tool and move the data from the csv file into a map when launching.

'''
universalD = {'\**/': []
    }
# def makedir(name):
#     current_directory = getcwd()
#     final_directory = path.join(current_directory, name)
#     if not path.exists(final_directory):
#         makedirs(final_directory)
#     else:
#         return False
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
def newSet(name):
    newSetDic = {
        "questions": [],
        "answers": []
    }
    while True:
        ipt = input("A: Enter a question you want to add to the library:\nB: quit\n")
        match ipt.upper():
            case "A":
                qt = input("Enter the question: ")
                if qt == "" or None:
                    print("Question can not be empty")
                newSetDic["questions"].append(qt)
                aw = input(("Enter the answer for the question\n",qt + ": "))
                if aw == "" or None:
                    print("Answer can not be empty")
                newSetDic["answers"].append(aw)
                print(newSetDic)
            case "B":
                writeToFile(name,newSetDic)
                break
            case _:
                print("Choose A or B")
        
def append(name):
    try:
        f = open(name,"a")
        newSet(name)
    except:
        print("File does not exist, making a new one")

        newSet(name)
def studySet(name):
    try:
        fn = name + "_data.txt"
        f = open(fn,"r")
        arr = []
        for x in f:
            arr.append(x)
        print("The questions will show up one at a time, press Q at any time to quit")
        
        for i in arr:
            temp = i.split(",")
            universalD[temp[0]] = temp[1]
        random.shuffle(arr)
        for i in arr:
            temp = i.split(",")
            print("Question:",temp[0])
            inp = input()
            match inp.upper():
                case "Q":
                    break
                case _:
                    pass
            print("The answer to:",temp[0],"is",universalD[temp[0]])
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
def inputs():
    while True:
        userInput = input("Select and option:\nA:new set of cards\nB:study an old set\nC:update an old set\nQ: quit\n")
        match userInput.upper():
            case "A":
                n = input("Enter the name of this new set, if set already exists the data will be appended to the existing file: ")
                newSet(n)
            case "B":
                nme = input("Enter the set you want to study: ")
                studySet(nme)
                
            case "C":
                nm = input("Enter the name of the set you want to append to: ")
                append(nm)
            case "Q":
                exit()
            case _:
                print("Please select a valid input: ")

inputs()               