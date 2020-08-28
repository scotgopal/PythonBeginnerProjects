import random
import os
import time
import sys
import numpy as np

# random.seed(1)

def playAgain():
    try:
        choice = int(input("Press 1 - Play again?\n\tOR\nNot 1 - Exit programme\t:"))
        if choice==1:
            gameStart()
        else:
            print("Programme exiting in 3s...\n")
            time.sleep(3)
            sys.exit()
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

def checkNumber(bigList, userGuess , halfCount):

    halfCount = halfCount+1
    print("\nHalving Process:", halfCount)
    bigList = sorted(bigList)
    halfA= []
    halfB = []

    medianValue = np.median(bigList)

    if medianValue in bigList: #total elements in List is ODD!
        # print("Present in List")
        medianIndex = bigList.index(medianValue)
        if userGuess == bigList[medianIndex]:
            print ("Found your number in the middle position during the", halfCount-1,"th halving process!\n")
            playAgain()
            pass
        halfA = bigList[:medianIndex]
        halfB = bigList[medianIndex+1:]
    else: #total elements in List is EVEN!
        medianPlusOne = bigList.index(medianValue+1) 
        halfA = bigList[:medianPlusOne] # does not include medianPlusOne meaning it registers exactly the first (n/2) elements
        halfB = bigList[medianPlusOne:] # includes medianPlusOne until the end meaning it registers exactly the second (n/2) elements
    
    if userGuess in halfA:
        print("First half selected")
        checkNumber (halfA, userGuess , halfCount)
    else:
        print("Second half selected")
        checkNumber (halfB, userGuess , halfCount)

def gameStart():

    # Create a random list of numbers with difference of 2 (How many numbers?)
    os.system('cls')
    print("------------------------------")
    print("--------BINARY SEARCH---------")
    print("------------------------------\n")
    print("Try to guess the number in the computer's random list of numbers!\n")
    
    global totalElements
    totalElements = random.randint(10, 50)
    # print("Total Elements:",totalElements)
    
    global fullNumberList 
    fullNumberList.append(random.randint(0,100))
    global currentElements 
    currentElements = len(fullNumberList)

    createList()

    sortedList = sorted(fullNumberList)

    print("Computer has prepared a list with", len(fullNumberList), "elements!\n")
    
    goodInput = False
    while (not goodInput):
        try:
            userGuess = int(input("Input your guess number:"))
            goodInput = True
        except ValueError:
            print("Input only an integer! Try again.\n")

    if userGuess in sortedList:
        print("Your number is in the list! Now we will see how many halves it takes to find your number.\n")
        halfCount = 0
        checkNumber(sortedList, userGuess, halfCount)
    else:
        print("Bad guess!\n")
        playAgain()

totalElements = 0
currentElements = 0
fullNumberList = []

gameStart()