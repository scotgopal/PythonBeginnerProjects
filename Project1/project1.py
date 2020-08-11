import random
import time
print("---------------------------")
print("--------GUESS GAME---------")
print("---------------------------")
print("This programme picks a number 0-20 and you need to guess it!\n")

n = random.randint(0,20)
trial = 0
while(1):
    while(1):
        try:
            guess = int(input("Guess a number between 0-20:")) #The input is in type <str>, typecasted to int
            break #can break only if input is a valid integer
        except ValueError:
            print("No valid integer! Please input again.\n") #Check input of the user

    if guess is n:            
        print("Congratulation! You guessed right!\n")
        print("Programme exiting in 3 seconds...")
        time.sleep(3)
        break
    elif guess > n:
        print("\nYou guessed higher. Guess again..")
        trial+=1
        print("Trial: ", trial,"\n")
    else:
        print("\nYou guessed lower. Guess again...")
        trial+=1
        print("Trial: ", trial,"\n")