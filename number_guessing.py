
import random

#generate the number
randomNum = random.randint(1, 100)

#loop to correct input
while True:
    try:
    #input number of user
        number = int(input("Guess a number between 1 and 100: "))

        if number > randomNum:
            print("Too High!")
        

        elif number < randomNum:
             print("Too Low!")
    
        else:
            print("Congratulations! You guessed the number.")
            break
    

    except ValueError:
        print("Please enter a valid number")
        




