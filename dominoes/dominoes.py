from itertools import combinations_with_replacement
from random import sample


def board():
    domino = list(map(lambda x: list(x), combinations_with_replacement(range(7), 2)))
    while True:
        player_bones = sample(domino, 7)
        pc_bones = sample(list(filter(lambda x: x not in player_bones, domino)), 7)
        stock_bones = list(filter(lambda x: x not in (player_bones + pc_bones), domino))
        player_doubles = [bones for bones in player_bones if len(set(bones)) == 1]
        pc_doubles = [bones for bones in pc_bones if len(set(bones)) == 1]
        doubles = player_doubles + pc_doubles
        if doubles:
            max_double = max(doubles)
            if max_double in player_doubles:
                player_bones.remove(max_double)
                first_player = "pc"
            else:
                pc_bones.remove(max_double)
                first_player = "player"
            return {'player': player_bones, 'pc': pc_bones,
                    'stock': stock_bones, 'snake': [max_double],
                    'turn': first_player}


 def board_status():
     if len(board['player']) == 0:
         return 'The game is over. You win!'
     elif len(board['pc']) == 0:
         return 'The game is over. The pc won!'
     snake = [num for bones in board['snake'] for num in bones]
     for i in range(7):
         if i in board['snake'][0] and i in board['snake'][-1] and snake.count(i) == 8:
             return "The game is over. It's a draw!"
     return 'game_not_done'


def play_board():
    print('=' * 70)
    print('Stock size:', len(board['stock']))
    print('Pc bones:', len(board['pc']))
    print()
    snake = board['snake']
    if len(snake) > 6:
        for i in range(3):
            print(snake[i], end='')
        print('...', end='')
        for i in range(-3, 0):
            print(snake[i], end='')
    else:
        for p in snake:
            print(p, end='')
    print()
    print('Your bones:')
    for i, bones in enumerate(board['player']):
        print(f'{i + 1}:{bones}')
    print()