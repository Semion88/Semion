import math
def CreditCalculator():
    print("What do you want to calculate?")
    print('type "m" for number of monthly payments,')
    print('type "p" for the monthly payment ,')
    x = input()
    if x == 'm':
        principal = int(input("Enter the loan principal:"))
        payment = int(input("Enter the monthly payment:"))
        interest = int(input("Enter the loan interest:"))
        x = payment / (payment - (interest/1200 * principal))
        degree = math.log(x, (interest / 1200 + 1))
        degree2 = math.ceil(degree)
        year = degree2 / 12
        round_up = round(year, (1))
        r = str(round_up)
        y = list(r)
        print("It will take", y[0], "years and", y[2], "months to repay this loan!")
    elif x == 'p':
        interest = float(input("Enter the loan interest:"))
        b = interest / 1200 * (1 + interest / 1200) ** float(input("Enter the monthly payment:"))
        c = (1 + interest / 1200) ** float(input("Enter the monthly payment:")) - 1
        e = b / c
        f = float(input("Enter the annuity payment:")) / e
        g = round(f)
        print("Your monthly payment =", g, "!")
    else:
        print("Pleas try again")

CreditCalculator()
