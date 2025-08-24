# Game Logic for Rock-Paper-Scissors

from random import randint

# List of players
choices = ["rock", "paper", "scissors"]

# Function to determine the outcome

def spin(user_choice):
    choose_number = randint(0, 2)
    computer_choice = choices[choose_number]
    
    if user_choice == "Rock":
        user_select_value = 0
    elif user_choice == "Paper":
        user_select_value = 1
    elif user_choice == "Scissors":
        user_select_value = 2

    if user_select_value == 0:
        if choose_number == 0:
            return "Tie! - Computer: Bad luck"
        elif choose_number == 1:
            return "YOU Lose - Computer: I am better"
        elif choose_number == 2:
            return "YOU Won - Computer: You won by luck"

    elif user_select_value == 1:
        if choose_number == 1:
            return "Tie! - Computer: Nice game"
        elif choose_number == 0:
            return "YOU Won - Computer: Shit how you are better"
        elif choose_number == 2:
            return "YOU Lose - Computer: booo"

    elif user_select_value == 2:
        if choose_number == 2:
            return "Tie!"
        elif choose_number == 0:
            return "YOU Lose - Computer: I am playing this game since I was born"
        elif choose_number == 1:
            return "YOU Won"