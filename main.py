import random
#Create tuple of move choices
choices = ("rock","paper","scissors")

#Ask player for choice
player_choice = input("Input your choice: ")

#Randomly generate computers choice
computer_choice = random.choice(choices)

#While loop incase of invalid input

    
while player_choice not in choices:
    print("Please select a choice (rock,paper,scissors): ")

if player_choice == computer_choice:
    print(f"You chose {player_choice} & Computer chose {computer_choice} It's a tie! ")
elif player_choice == "rock" and computer_choice == "scissors":
    print(f"You chose {player_choice} & Computer chose {computer_choice} You win! ")
elif player_choice == "paper" and computer_choice == "rock":
    print(f"You chose {player_choice} & Computer chose {computer_choice} You win! ")
elif player_choice == "scissors" and computer_choice == "paper":
    print(f"You chose {player_choice} & Computer chose {computer_choice} You win! ")
else:
    print(f"You chose {player_choice} & Computer chose {computer_choice} You lose :( ")
    
play_again = input("Would you like to play again? (y/n) ")
if not play_again == "y":
    running = False

