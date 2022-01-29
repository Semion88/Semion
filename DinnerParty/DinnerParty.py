import random

friends = int(input("Enter the number of friends joining (including you):\n"))
new_dict = {}

if friends > 0:
    print("Enter the name of every friend (including you), each on a new line:\n")
    name = [input() for i in range(friends)]
    new_dict = {name[x - 1]: 0 for x in range(friends + 1)}
    Summa = int(input("Enter the total amount:"))
    s = Summa / friends
    z = round(s, 2)
    new_dict = {name: z for name in new_dict}
    print(new_dict)
    while True:
        g = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if g == 'Yes':


        else:
            print('No one is going to be lucky')
            new_dict = {name: z for name in new_dict}
            print(new_dict)
            break
