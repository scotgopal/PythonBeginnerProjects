import random
import os
import time

replay = True

def playAgain():
    try:
        choice = int(input("Press 1 - Play again?\n\tOR\nNot 1 - Exit programme\t:"))
        if choice==1:
            pass
        else:
            print("Programme exiting in 3s...\n")
            time.sleep(3)
            global replay 
            replay = False
    except ValueError:
        print("Invalid choice, try again...\n")
        playAgain()

def createList():
    global currentElements
    while currentElements != totalElements:
        i = random.randint(0,100)
        if i not in fullNumberList:
            if i-2 in fullNumberList: 
                fullNumberList.append(i)
                currentElements = len(fullNumberList)
            elif i+2 in fullNumberList:
                fullNumberList.append(i)
                currentElements = len(fullNumberList)
        else:
            pass

def checkNumber(userGuess):
    
    if userGuess == median(fullNumberList):


while(replay):

    # Create a random list of numbers with difference of 2 (How many numbers?)
    os.system('cls')
    print("------------------------------")
    print("--------BINARY SEARCH---------")
    print("------------------------------\n")
    print("Try to guess the number in the computer's random list of numbers!\n")
    
    totalElements = random.randint(10, 50)
    # print("Total Elements:",totalElements)
    
    fullNumberList = []
    fullNumberList.append(random.randint(0,100))
    # print("First Element:", fullNumberList[0])
    currentElements = len(fullNumberList)

    createList()

    sortedList = sorted(fullNumberList)
    # print("Sorted List:",sortedList)

    print("Computer has prepared a list with", len(fullNumberList), "elements!\n")
    
    goodInput = False
    while (not goodInput):
        try:
            userGuess = int(input("Input your guess number:"))
            goodInput = True
        except ValueError:
            print("Input only an integer! Try again.\n")

    checkNumber(userGuess)

    # playAgain()
    break

listA = []
for i in range(25) :
    listA.append(i)

def halving():
    length = len(listA)
    length/=length
    if length is float:
        length = round(length)
        

