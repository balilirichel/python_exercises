import random

roll = 0

while True:

    choice = input("Roll the dice? (y/n): ")
    
    if choice.lower()== 'y':

        dice = int(input("How many dice do you want to roll?: "))
        # die1 = random.randint(1, 6)
        # die2 = random.randint(1,6)
        # print(f'({die1}, {die2})')
        i = 0
        while i < dice:
            die1 = random.randint(1, 6)
            die2 = random.randint(1,6)
            print(f'({die1}, {die2})')
            i += 1
            roll += 1
    
    

    elif choice.lower() == 'n':
        print("You have rolled a total of " + str(roll) + "dices")
        print("Thanks for playing!")
        break
    else: 
        print("Invalid Choice")
