import string
import random
import os
import time
import sys

# file = open(os.path.join(sys.path[0],"sowpods.txt"))
# file = open("Project5\sowpods.txt")
file = open("sowpods.txt")
wordsWithNewLine = file.readlines()
file.close()

cleanWords = []

for words in wordsWithNewLine:
    if words.endswith('\n'):
        replacedWord = words.replace('\n','')
        cleanWords.append(replacedWord)

def list2Str(inputList):
    outputString = ''
    for index in inputList:
        outputString+=index
    return outputString

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

def guessProcess():
    try:
        print('\n~~~Guessing Time~~~')
        print("Correct Letters\t:", rightLetters)
        print('Wrong Letters\t:', wrongLetters,'\n')
        if mistakeCount <6:
            trial = (input("What is your guess:")).lower()
            if trial not in string.ascii_letters:
                print("\nThis version of Hangman no numbers and single alphabets only, smartie!")
                raise ValueError
            elif trial in rightLetters:
                print("That is already correct, genius. Try something else.\n")
                guessProcess()
            elif trial in wrongLetters:
                print("There's 26 alphabets, and you got wrong for that already!\n")
                guessProcess()
            else:
                pass
            letterCheck(trial)
        else:
            print('You LOST!\n')
            print('The correct word was:\n>>>>',selectedWord,'<<<<\n')
            playAgain()
    except ValueError:
        guessProcess()

def letterCheck(trial):
    if trial in selectedWordList:
        rightLetters.append(trial)
        guessIndex = -1
        for element in selectedWordList:
            guessIndex+=1
            if element == trial:
                global guessed #Call global variable guessed into the function
                guessedList = list(guessed)
                guessedList[guessIndex] = trial
                guessed = list2Str(guessedList)       
        if guessed == selectedWord:
            print(len(selectedWord),"-letter word: " + guessed)
            print("CONGRATULATIONS! YOU WIN!")
            playAgain()

        else:
            print("\nAmazing!\n")
            print(len(selectedWord),"-letter word: " + guessed)
            print("Guess again!\n")
            guessProcess()
    else:
        wrongLetters.append(trial)
        global mistakeCount
        mistakeCount+=1
        print("Ooopsie... Wrong guess. You have", 6-mistakeCount,"tries(/try) left!\n")
        print(len(selectedWord),"-letter word: " + guessed)
        guessProcess()


replay = True
while(replay):
    os.system("cls")
    print("------------------------")
    print("--------HANGMAN---------")
    print("------------------------\n")
    print("Let's play a fun game of Hangman! You get 6 chances to guess the whole word!\n")
    # random.seed(3)
    selectedWord = random.choice(cleanWords)
    # print("Selected word: ", selectedWord)
    guessed = "-"*len(selectedWord)
    print('Challenge: \nGuess this', len(selectedWord),"-letter word: " + guessed)
    selectedWordList = list(selectedWord)
    
    mistakeCount = 0
    rightLetters = []
    wrongLetters = []
    
    guessProcess() #jump to guess function