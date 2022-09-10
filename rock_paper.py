#Paper Rock Scissors Game

#Import Module
import random

#Define objects in List
choice_list = ("rock", "paper", "scissors")

#Begin game with opening question
print("Welcome to Paper Rock Scissors Game ")
#Ask for game permission, sets assignment to lowercase and variable
join = input (" Would you like to play a game?    ").lower()
#States if assigned variables starts with letter 'y' then proceed
if join.startswith('y'):
    print ("Great," + " Let's play a game ")
#If assigned variable doesn't start with letter 'y' then end
else:
    print ("Maybe some other time ")
 
#User inputs choice which is then printed    
player_choice = input ("Player one please choose: rock  paper or scissors    ")
print ("Your choice is: ", player_choice)

#PC choose and print random choice
computer_choice = print("Computer's choice is: " + random.choice(choice_list))
    
#Decision path  
if player_choice == computer_choice:
    print ("Both players selected {player_choice}, the game is a tie!")
elif player_choice == "rock":
    if computer_choice == "paper":
        print("Paper covers rock, computer wins")
    else:
        print("Rock crushes scissors, player wins")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock, player wins")
    else:
        print("Scissors cut paper, computer wins")
elif player_choice == "scissors":
    if computer_choice == "rock":
        print("Rock crushes scissors, computer wins")
    else:
        print("Scissors cut paper, player wins")



