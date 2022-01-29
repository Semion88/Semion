print('Write how many ml of water the coffee machine has:')
water = int(input())
print('Write how many ml of milk the coffee machine has:')
milk = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
beans = int(input())
print('Write how many cups coffee you need ? :')
cups = int(input())
Cups = water // 200 or milk // 50 or beans // 15

if cups > Cups:
    print('No, I can make only ' + str(Cups) + ' cups of coffee.')
elif cups == Cups:
    print('Yes, I can make that amount of coffee.')
else:
    newCups = Cups - cups
    print('Yes, I can make that amount of coffee (and even ' + str(newCups) + ' more than that)')
