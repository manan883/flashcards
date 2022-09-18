from sys import exit
from os import getcwd
from os import path
from os import makedirs
'''
ask user to enter question and answer
put in a map
store question and answer in a csv file with a , as a seperator 
when quizzing user the comma as a parse tool and move the data from the csv file into a map when launching.

'''
def makedir(name):
    current_directory = getcwd()
    final_directory = path.join(current_directory, name)
    if not path.exists(final_directory):
        makedirs(final_directory)
    else:
        return False
def writeToFile(name,dataDict):
    fn = str(name + ".txt")
    try:
        
        f = open(fn,"x")
    except:
        pass
    ap = open(fn,"a")
    for i,j in zip(dataDict["questions"], dataDict["answers"] + "\n"):
        ap.write(i + "," + j)
        #print(i + "," + j)
    pass
def newSet(name):
    newSetDic = {
        "questions": [],
        "answers": []
    }
    val = makedir(name)
    if val == False:
        print("directory exists already")
        return 
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
        

def inputs():
    while True:
        userInput = input("Select and option:\nA: new set of cards\nB:study and old set\nC:update and old set\nQ: quit\n")
        match userInput.upper():
            case "A":
                newSet("name")
            case "B":
                print
            case "C":
                print
            case "Q":
                exit()
            case _:
                print("Please select a valid input: ")

inputs()               