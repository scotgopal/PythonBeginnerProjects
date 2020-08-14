import random
import string
import os

newPass = True
while(newPass):
    os.system("cls")
    print("---------------------------------------")
    print("----------PASSWORD GENERATOR-----------")
    print("---------------------------------------")
    print("\nThis programme generates a password for you based on your preference!\n")

    while(1):
        def symbolF():
            symbolCount = int(input("How many symbols do you want? (<=8)\n"))
            if symbolCount>8:
                print("Too many symbols. Input again.\n")
                symbolF()
            return symbolCount

        try:
            letterCount = int(input("How many alphabets do you want?\n"))
            numberCount = int(input("How many numbers do you want?\n"))
            symbolCount = symbolF()
            
            totalCount = letterCount + numberCount + symbolCount
            if totalCount>=6:
                break
            else:
                print("Invalid total. Minimum 6 characters.\n")

        except ValueError:
            print("Invalid input. Try again.\n")

    all_Letters = string.ascii_letters
    all_Numbers = string.digits
    all_Symbols = ["!","@","#","$","%","&","*","?"]

    letterList = random.choices(all_Letters, k = letterCount)
    numberList = random.choices(all_Numbers, k = numberCount)
    symbolList = random.choices(all_Symbols, k = symbolCount)

    print("\nAlphabets", letterList)
    print("Numbers", numberList)
    print("Symbols", symbolList,"\n")

    passList = letterList + numberList + symbolList
    shuffledList = random.sample(passList, len(passList))
    
    fullPass=""
    for each in shuffledList:
        fullPass+=each

    print("YOUR PASSWORD IS - ", fullPass,"\n")

    def finalStep():
        try:
            choice = int(input("1 - Create another password\n\tOR\nOther - Exit programme\t:"))
            if choice==1:
                pass
            else:
                print("Programme exiting...\n")
                global newPass 
                newPass = False
        except ValueError:
            print("Invalid choice, try again...\n")
            finalStep()
    
    finalStep()