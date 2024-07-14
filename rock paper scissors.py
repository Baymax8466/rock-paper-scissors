import random

user_wins = 0
computer_wins = 0

options = ["Rock" , "Paper" , "Scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit : ").lower()
    if user_input == "Q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # Rock: 0 , Paper: 1 , Scissors: 2
    computer_pick = options[random_number] 
    print("computer picked", computer_pick + ".")

    if user_input == "Rock" and computer_pick == "Scissors":
        print(" YOU WON !! ")
        user_wins += 1

    elif user_input == "Paper" and computer_pick == "Rock":
        print(" YOU WON !! ")
        user_wins += 1

    elif user_input == "Scissors" and computer_pick == "Paper":
        print(" YOU WON !! ")
        user_wins += 1
        
    else:
        print("!! YOU LOST !!")
        computer_wins += 1
        
print("YOU WON", user_wins , "times.")
print(" THE COMPUTER WON ", computer_wins , "times.")
print("!! GOODBYE !!")