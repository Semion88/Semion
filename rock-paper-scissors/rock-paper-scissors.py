from random import choice

print("Welcome To Rock-Paper-Scissors")
player = input("Select any option\nrock\npaper\nscissors ").strip().lower()
computer = choice("rps")
if player == computer:
    print("Draw")
    print("Computer's choice -> ", computer)
elif player == "rock" and computer == "scissors" or player == "paper" and computer == "rock" or player == "scissors" and computer == "paper":
    print("Player Wins")
    print("Sorry, but the computer chose another option and failed:", computer)
else:
    print("Enter another word")
    print("Sorry, but the computer chose another option:", computer)