from random import choice

print("Welcome To Rock-Paper-Scissors")
values = {
    'rock': ['gun', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['fire', 'scissors', 'wolf', 'tree', 'human', 'snake'],
    'scissors': ['gun', 'lightning', 'devil', 'dragon', 'water', 'rock'],
    'gun': ['water', 'air', 'sponge', 'paper', 'devil', 'dragon'],
    'lightning': ['water', 'air', 'sponge', 'paper', 'dragon', 'wolf'],
    'devil': ['water', 'air', 'sponge', 'paper', 'tree', 'wolf'],
    'dragon': ['air', 'sponge', 'paper', 'tree', 'wolf', 'human'],
    'water': ['snake', 'sponge', 'paper', 'tree', 'wolf', 'human'],
    'air': ['snake', 'sponge', 'scissors', 'tree', 'wolf', 'human'],
    'sponge': ['snake', 'scissors', 'tree', 'human', 'rock', 'fire'],
    'wolf': ['snake', 'scissors', 'human', 'rock', 'fire', 'gun'],
    'tree': ['snake', 'scissors', 'rock', 'fire', 'gun', 'lightning'],
    'human': ['scissors', 'rock', 'fire', 'gun', 'lightning', 'devil'],
    'snake': ['rock', 'fire', 'gun', 'lightning', 'devil', 'dragon'],
    'fire': ['fire', 'gun', 'lightning', 'devil', 'dragon', 'water'],
}


def is_player_won(player_word, computer_word):
    is_win = True
    for word in values[player_word]:
        if word == computer_word:
            is_win = False
    return is_win


while True:
    player_input = input(
        "Select any option\nrock\npaper\nscissors\ngun\nlightning\ndevil\ndragon\nwater\nair\nsponge\nwolf\ntree\nhuman\nsnake\nfire\nexit\n ").strip()
    computer_input = choice( ['rock', 'paper', 'scissors', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'sponge', 'wolf', 'tree',
         'human', 'snake', 'fire'])
    if player_input == computer_input:
        print("Draw")
        print("Computer's choice -> ", computer_input)
    elif is_player_won(player_input, computer_input):
        print("Player Wins")
        print("Computer chose: ", computer_input)
    elif not is_player_won(player_input, computer_input):
        print("Computer Wins")
        print("Computer chose: ", computer_input)
    else:
        print("Enter another word")
        print("Sorry, but the computer chose another option:", computer_input)
    if player_input == "exit":
        break