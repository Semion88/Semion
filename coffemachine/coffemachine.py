#По умолчанию
water = 400
milk = 540
beans = 120
cups = 9
money = 550
v = input
#ингридиентов в кофеварке
def machine_have():
    print()
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')
    print()

print("Write variants (buy, fill, take,remaining,exit):")

print(machine_have)
print()
#функция, для покупки кофе
def buy():
    print("What do you want to buy?:\n"
          "1 - espresso\n"
          "2 - latte\n"
          "3 - cappuccino"
          "4 - back to menu")
    type = input()

    def espresso():
        global water,beans,money,cups,milk
        water = water - 250
        beans = beans - 16
        money = money + 4
        cups = cups - 1
    def latte():
        global water,beans,money,cups,milk
        water = water - 350
        milk = milk - 75
        beans = beans - 20
        money = money + 7
        cups = cups - 1
    def cappuccino():
        global water,beans,money,cups,milk
        water = water - 200
        milk = milk - 100
        beans = beans - 12
        money = money + 6
        cups = cups - 1
    if type == "1":
        espresso()
    elif type == "2":
        latte()
    else:
        cappuccino()
#  функция, для изьятия денег из машины
def take():
    global money
    print("I gave you " + str(money)+"gryven")
    money = 0
# функция,для наполнения кофемашины
def fill():
    global water,beans,cups,milk
    print("Write how many ml of water do you want to add:")
    water_filled = int(input())
    print("Write how many ml of milk do you want to add:")
    milk_filled = int(input())
    print("Write how many grams of coffee beans do you want to add:")
    beans_filled = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    cups_added = int(input())
    water = water + water_filled
    milk = milk + milk_filled
    beans = beans + beans_filled
    cups = cups + cups_added
if v == "buy":
    buy()
elif v == "take":
    take()
else:
    fill()

print()
print("The cofee machine has:")
print(str(water) + " of water")
print(str(milk) + " of milk")
print(str(beans) + " of coffee beans")
print(str(cups) + " of disposable cups")
print(str(money) + " of money")
def main():
    while True:
        action = machine_have()
        if action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            take()
        elif action == 'exit':
            break
        elif action == 'remaining':
            machine_have()
