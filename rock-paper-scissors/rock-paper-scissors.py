from random import choice

print("Welcome To R-P-S")
player = input("Select any option\nrock\npaper\nscissors ").strip().lower()
computer = choice("rock,paper,scissors")
if player==computer:
    print("Draw")
    print("Computer's choice -> ",computer)
elif player=="rock" and computer=="paper" or player=="paper" and computer=="scissors" or player=="scissors" and computer=="rock":
    print("Computer's choice -> ",computer)
else:
    print("Enter another word")
    print("Sorry, but the computer chose another option:",computer)