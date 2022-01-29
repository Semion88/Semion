import random

friends = int(input("Enter the number of friends joining (including you):"))

if friends > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    name = [input() for i in range(friends)]
    new_dict = {name[x - 1]: 0 for x in range(friends + 1)}
    sum = int(input("Enter the total amount: "))
    new_dict_keys = list(new_dict.keys())
    new_dict_keys.sort()


    while True:
        answer = input('Do you want to use the "Who is lucky?" feature? Write y/n:')
        if answer == 'y':
            list_amount = [round((sum / (friends - 1)), 2)] * friends
            lucky_friend_index = random.choice(range(friends))
            for i in range(len(new_dict_keys)):
                new_dict[new_dict_keys[i]] = list_amount[i]
            new_dict[new_dict_keys[lucky_friend_index]] = 0
            print(f"{new_dict_keys[lucky_friend_index]} is the lucky one!")
            print(new_dict)
            break
        elif answer == "n":
            list_amount = [round((sum / friends), 2)] * friends
            for i in range(len(new_dict_keys)):
                new_dict[new_dict_keys[i]] = list_amount[i]
            print("No one is going to be lucky.")
            print(new_dict_keys)
            break
        else:
            print("Incorrect choice. Try again!")
