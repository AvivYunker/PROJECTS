def between_ranges (lower, upper, digit, count):
    lower = int(lower)
    upper = int(upper)
    digit = int(digit)
    count = int(count)
    while (lower <= upper):
        results = is_digit_count(lower, digit, count)
        if (results == 1):
            print(str(lower) + " is an option")
        lower = int(lower + 1)

def is_digit_count (num, digitReal, cntReal):
    num = int(num)
    digitReal = int(digitReal)
    cntReal = int(cntReal)
    cntTemp = int(0)
    while (num > 0):
        temp = int(num % 10)
        if (temp == digitReal):
            cntTemp = int(cntTemp + 1)
        num = int(num / 10)
    if (cntTemp == cntReal):
        return 1
    else:
        return 0



lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")
dig = input("The digit?\n")
cnt = input("How many of " + str(dig) + "?\n")

lwr = int(lwr)
upr = int(upr)
dig = int(dig)
cnt = int(cnt)

between_ranges(lwr, upr, dig, cnt)
input("\nDONE!\n")
