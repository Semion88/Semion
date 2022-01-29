print("How many cups you need ?:")
cups = input()
print('For ' + str(cups) + ' cups of coffee you will need:')
water = cups * 200
milk = cups * 50
beans = cups * 15
print(str(water) + ' ml of water')
print(str(milk) + ' ml of milk')
print(str(beans) + ' ml of coffee beans')
print("""
1-Starting to make a coffee
2-Grinding coffee beans
3-Boiling water
4-Mixing boiled water with crushed coffee beans
5-Pouring coffee into the cup
6-Pouring some milk into the cup
7-Coffee is ready!""")

