friends = int(input("Enter the number of friends joining (including you):"))


if friends > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    name = [input() for i in range(friends)]
    new_dict = {name[x - 1]: 0 for x in range(friends + 1)}
    print(new_dict)
    Summa = int(input("Enter the total amount:"))
    if int(Summa / friends) != (Summa / friends):
        New_Summa = [round((Summa / friends), 2)] * friends
    else:
        New_Summa = [round(Summa / friends)] * friends
    new_dict_keys = list(new_dict.keys())
