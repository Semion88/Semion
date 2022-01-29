import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--interest')
parser.add_argument('--annuity')
parser.add_argument('--payment')
parser.add_argument('--periods')
arg = parser.parse_args()

type = arg.type
principal = arg.principal
interest = arg.interest
annuity = arg.annuity
payment = arg.payment
periods = arg.periods

print(principal, interest, annuity, periods, payment,type)

try:
    if principal:
        p = int(principal)
        if periods:
            per = int(periods)
            if interest:
                percent = int(interest)
                interest = percent / (12 * 100)
                if percent != 0:
                    interest = float(percent)
                    i = percent / (12 * 100)
                    m = 1
                    D = 0
                    while m <= per:
                        d = (p / per) + (i * (p - (p * (m - 1) / per)))
                        print("Month {}: paid out {}".format(m, math.ceil(d)))
                        m += 1
                        D += math.ceil(d)
                        print("Overpayment = {}".format(D - d))
                else:
                    print("Incorrect Par2")
            else:
                print("Incorrect Par3")
        else:
            print("Incorrect Par4")
    else:
        print("Incorrect Par5")
except Exception:
    print("Incorrect Parameters1")

try:
    if principal:
        p = int(principal)
        if payment:
            pay1 = int(payment)
            if interest:
                percent = int(interest)
                interest = percent / (12 * 100)
                if percent:
                    percent = float(interest)
                    i = percent / (12 * 100)
                    x = int(pay1) / (int(pay1) - (interest / 1200 * int(p)))
                    degree = math.log(int(pay1) / (int(pay1) - (interest / 1200 * int(p))),
                                      (1 + interest / 1200))
                    year = math.ceil(degree) / 12
                    r = str(round(year, (1)))
                    print("It will take", list(r)[0], "years and", list(r)[2], "months to repay this loan!")
                    print("Overpayment =", p * math.ceil(degree) - int(pay1))
                else:
                    print("Incorrect Par6")
            else:
                print("Incorrect Par7")
    else:
        print("Incorrect Par9")
except Exception:
    print("Incorrect Parameters2")

try:
    if periods:
        periods = int(periods)
        if payment:
            payment2 = int(payment)
            if interest:
                percent = int(interest)
                interest = percent / (12 * 100)
                if percent == interest:
                    percent = float(interest)
                    i = percent / (12 * 100)
                    number = pow(1 + i, int(periods))
                    a = i * (1 + i) ** int(periods)
                    b = (1 + i) ** int(periods) - 1
                    c = i * (1 + i) ** int(periods) / (1 + i) ** int(periods) - 1
                    d = float(payment2) / i * (1 + i) ** int(periods) / (1 + i) ** int(periods) - 1
                    result = math.floor(float(float(payment) / ((i * number) / (number - 1))))
                    print("Your loan principal =", round(d), "!")
                    print('Overpayment =', float(payment2) * int(periods) - result)
                else:
                    print("Incorrect Par10")
            else:
                print("Incorrect An11")
    else:
        print("Incorrect Par13")
except Exception:
    print("Incorrect Parameters3")
