import random

print("Let's play Rock-Paper-Scissors!")
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

while True:
    user_choice = input("Choose rock, paper, or scissors (or 'quit' to end the game): ")
    user_choice = user_choice.lower() # convert input to lowercase for consistency
    
    if user_choice == "quit":
        print("Thanks for playing!")
        break
        
    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue # restart the loop if user input is invalid
    
    print(f"You chose {user_choice}, and the computer chose {computer_choice}.")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose!")
    
    computer_choice = random.choice(options) # update computer's choice for next round
