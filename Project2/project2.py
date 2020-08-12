import random
import time
import sys
import os

while(1):
    def playagain(): #function to request if users want to replay
        while(1):
            replay = ((input("Do you want to play again? (y/n): ")).lower()).strip()
            
            if replay not in ("y","n"):
                print("Invalid input! Try again")
            else:
                break
        
        if replay =="n":
            print("\nProgramme exiting in 3s...")
            time.sleep(3)   #for 3 second time delay
            sys.exit()  #exits the programme
            
            
    os.system('cls') #clears the terminal
    print("------------------------------------")
    print("--------Schere|Stein|Papier---------")
    print("------------------------------------\n")
    print("Play rock, paper, scissor with the programme!\n")

    whatToThrow = ["rock", "paper", "scissor"] #a list of choices
    computerChoice = random.choice(whatToThrow) #randomizing selection from the list

    while(1): #a while loop to ensure valid input from user
        print("Between [rock, paper, scissor]")
        userChoice = ((input("What is your choice? ")).lower()).strip()
        
        if userChoice not in whatToThrow:
            print("Invalid input. Try again.\n")
        else:
            break
        
    print("\nYour Choice\t:",userChoice.capitalize())
    print("Computer Choice\t:",computerChoice.capitalize(),"\n")

    if userChoice==computerChoice:
        print("Its a tie!")
        playagain()

    elif userChoice == whatToThrow[0]:
        if computerChoice == whatToThrow[1]:
            print("You lost!")
            playagain()
        else:
            print("You win!")
            playagain()
    elif userChoice == whatToThrow[1]:
        if computerChoice == whatToThrow[2]:
            print("You lost!")
            playagain()
        else:
            print("You win!")
            playagain()
    elif userChoice == whatToThrow[2]:
        if computerChoice == whatToThrow[0]:
            print("You lost!")
            playagain()
        else:
            print("You win!")
            playagain()
