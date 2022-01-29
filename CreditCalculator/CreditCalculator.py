import math
import sys
try:
    args = sys.argv
    type = args[1]
    if type == "--type=diff":
        p = args[2]
        if p[:12] == "--principal=":
            p = int(p[12:])
            n = args[3]
            if n[:10] == "--periods=":
                n = int(n[10:])
                i_percent = args[4]
                if i_percent[:11] == "--interest=":
                    i_percent = float(i_percent[11:])
                    i = i_percent / (12 * 100)
                    m = 1
                    D = 0
                    while m <= n:
                        d = (p/n) + (i*(p - (p*(m-1)/n)))
                        print("Month {}: paid out {}".format(m, math.ceil(d)))
                        m += 1
                        D += math.ceil(d)
                    print("Overpayment = {}".format(D - p))
                else:
                    print("Incorrect Parameters")
            else:
                print("Incorrect Parameters")
        else:
            print("Incorrect Parameters")
    elif type == '--type=annuity':
        if args[2][:12] == '--principal=':
            p = int(args[2][12:])
            if args[3][:10] == '--payment=':
                a = int(args[3][10:])
                interest = args[4]
                if interest[:11] == '--interest=':
                    interest = float(interest[11:])
                    i = interest / 1200
                    x = int(a[10:]) / (int(a[10:]) - (interest / 1200 * int(args[2][12:])))
                    degree = math.log(int(a[10:]) / (int(a[10:]) - (interest / 1200 * int(args[2][12:]))), (1 + interest/ 1200))
                    year = math.ceil(degree) / 12
                    round_up = round(year, (1))
                    r = str(round_up)
                    y = list(r)
                    print("It will take", y[0], "years and", y[2], "months to repay this loan!")
                    #print("Overpayment =", args[3] * math.ceil(degree)-int(p[12:]))
                else:
                    print("Incorrect Parameters")
            else:
                print("Incorrect Parameters")
        elif args[2][:10] == '--payment=':
            if args[3][:10] == '--periods=':
                interest = args[4]
                if interest[:11] == '--interest=':
                    interest = float(interest[11:])
                    i = interest / 1200
                    num = pow(1 + i, int(args[3][10:]))
                    a = i * (1 + i) ** int(args[3][10:])
                    b = (1 + i) ** int(args[3][10:]) - 1
                    c = i * (1 + i) ** int(args[3][10:]) / (1 + i) ** int(args[3][10:]) - 1
                    d = float(args[2][10:]) / i * (1 + i) ** int(args[3][10:]) / (1 + i) ** int(args[3][10:]) - 1
                    z = round(d)
                    result_p = math.floor(float(float(args[2][10:]) / ((i * num) / (num - 1))))
                    print("Your loan principal =", round(d), "!")
                    print('Overpayment =', float(args[2][10:]) * int(args[3][10:]) - result_p)
                else:
                    print("Incorrect Parameters")
            else:
                print("Incorrect Parameters")
        else:
            print("Incorrect Parameters")
    else:
        print("Incorrect Parameters")


except Exception:
    print("Incorrect Parameters")
