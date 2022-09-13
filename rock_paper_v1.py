# Paper Rock Scissors Game

#Import Module
import random
import sys

while True:
    player_choice = input("Enter a choice (rock, paper, scissors)")
    choice_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choice_list)
    print(f"\nYou chose {player_choice}, computer chose {computer_choice}. \n")
    
    if player_choice == computer_choice:
        print(f"\nBoth players selected {player_choice}, the game is a tie. \n")
    elif player_choice == "rock":
        if computer_choice == "paper":
            print("Paper covers rock, computer wins")
        else:
            print("Rock crushes scissors, player wins")
    elif player_choice == "paper":
        if computer_choice == "scissors":
            print("Scissors cut paper, computer wins")
        else:
            print("Paper covers rock, player wins")
    elif player_choice == "scissors":
        if computer_choice == "rock":
            print("Rock crushes scissors, computer wins")
        else:
            print("Scissors cut paper, player wins")
            
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    