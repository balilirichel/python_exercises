import random

#computer choice
possible_actions = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_actions)

while True:

    #input user choice  
    user_choice = input("Rock, Paper and Scissors? (r/p/s):  ").lower()
        
    choices = ['r', 'p', 's']

    if user_choice not in choices:
        print("Invalid Choice")

    else:  
        if user_choice == computer_choice:
            print("It's a tie")
        elif user_choice == "r":
            if computer_choice == "paper":
                print("You choose rock")
                print("Computer choose paper")
                print("You lose")
                
            else:
                print("You choose rock")
                print("Computer choose scissors")
                print("You win")
                
        elif user_choice == "p":
            if computer_choice == "scissors":
                print("You choose paper")
                print("Computer choose scissors")
                print("You lose")
            
            else:
                print("You win")
                print("You choose paper")
                print("Computer choose rock")
        
        elif user_choice == "s":
            if computer_choice == "rock":
                print("You choose scissors")
                print("Computer choose rock")
                print("You lose")
                
            else:
                print("You choose scissors")
                print("Computer choose paper")
                print("You win")

        else:
            print("Invalid Choice")
    
        continuePlaying = input("Continue? (y/n): ").lower()

        if continuePlaying == "n":
            break
        else:
            continue
