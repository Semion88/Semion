from itertools import combinations_with_replacement
from random import sample, choice


# sample () - это встроенная функция модуля random в Python, которая возвращает список элементов определенной длины, выбранных из последовательности, то есть списка, кортежа, строки или набора

#основа поля для игры
def board():
    domino = list(map(lambda x: list(x), combinations_with_replacement(range(7), 2)))
# lambda- выражения в Python позволяют функции быть созданной и переданной(зачастую другой функции) в одной строчке кода.
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

#определение:победа,ничья,поражение
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

#таблица
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

#справление ошибок
def move_on_board(move):
    try:
        move = int(move)
    except ValueError:
        return False

    return len(board['player']) >= abs(move)

#ход , после которго, забирается одна из 6 костяшек
def make_move(move, player):
    if move == 0:
        stock_bones = choice(board['stock'])
        board['stock'].remove(stock_bones)
        board[player].append(stock_bones)
        return
    index = abs(move) - 1
    bones = board[player][index]
    board[player].remove(bones)
    if move > 0:
        board['snake'].append(bones)
    else:
        board['snake'].insert(0, bones)

#  игра
board = board()
while True:
    play_board()
    game_state = board_status()

    if game_state != 'game_not_done':
        print('Status:', game_state)
        break

    turn = board['turn']
    if turn == 'player':
        print("Status: It's your turn to make a move. Enter your command:")
        while True:
            move = input()
            if move_on_board(move):
                break
            print('Invalid input. Please try again.')
        move = int(move)
        board['turn'] = 'pc'
    else:
        input('Status: Pc is about to make a move. Please push Enter')
        move = choice(range(-len(board['pc']), len(board['pc'])))
        board['turn'] = 'player'

    make_move(move, turn)