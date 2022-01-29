money = 550
water = 400
milk = 540
beans = 120
cups = 9

class CustomError(Exception):
    pass

def print_state():
    print()
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')
    print()

def select_action() -> str:
    print("ATTENCION!!! Вы должны написать не цифры , а слова англ !")
    return input('Write action:\n 1-купить(buy)'
                 '\n 2-наполнить(fill)'
                 '\n 3-взять(take)'
                 '\n 4-повторить(remaining)'
                 '\n 5-выход(exit)\n:')

def select_coffe() -> int:
    print()
    move = input('What do you want to buy?'
                 ' 1 - espresso,'
                 ' 2 - latte,'
                 ' 3 - cappuccino,'
                 ' 4 - back to main menu: ')
    if move == '4':
        return 0
    return int(move)


def is_enough(n_water=0, n_milk=0, n_beans=0):
    if water < n_water:
        print('Sorry, not enough water!\n')
        raise CustomError
    if milk < n_milk:
        print('Sorry, not enough milk!\n')
        raise CustomError
    if beans < n_beans:
        print('Sorry, not enough beans!\n')
        raise CustomError
    if cups < 1:
        print('Sorry, not enough cups\n')
        raise CustomError
    print('I have enough resources, making you a coffee!\n')


def buy():
    global money, water, milk, beans, cups

    variants = select_coffe()

    try:
        if variants == 0:
            pass
        elif variants == 1:  # espresso
            is_enough(n_water=250, n_beans=16)

            money += 4
            water -= 250
            beans -= 16
            cups -= 1
        elif variants == 2:  # latte
            is_enough(n_water=350, n_milk=75, n_beans=20)

            money += 7
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
        elif variants == 3:  # cappuccino
            is_enough(n_water=200, n_milk=100, n_beans=12)

            money += 6
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
        else:
            raise ValueError(f'Unknown variant {variants}')
    except CustomError:
        pass


def fill():
    global water, milk, beans, cups

    print()
    water += int(input('Write how many ml of water do you want to add: '))
    milk += int(input('Write how many ml of milk do you want to add: '))
    beans += int(input('Write how many grams of coffee beans'
                       ' do you want to add: '))
    cups += int(input('Write how many disposable cups of coffee'
                      ' do you want to add: '))
    print()


def take():
    global money

    print()
    print(f'I gave you {money} griven')
    print()

    money = 0


def menu():
    while True:
        action = select_action()

        if action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            take()
        elif action == 'exit':
            break
        elif action == 'remaining':
            print_state()
        else:
            raise ValueError(f'Unknown command {action}')

menu()

