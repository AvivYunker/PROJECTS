def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        results = is_special_armstrong(lower)
        if (results == 1):
            print(str(lower) + " is a special Armstrong")
        lower = int(lower + 1)

def is_special_armstrong (num):
    num = int(num)
    sumD = sum_digits(num)
    cntD = digit_counter(num)
    temp = pow(sumD, cntD)
    if (num == temp):
        return 1
    else:
        return 0

def sum_digits (num):
    num = int(num)
    sums = int(0)
    while (num > 0):
        temp = int(num % 10)
        sums = int(sums + temp)
        num = int(num / 10)
    return sums


def digit_counter (num):
    num = int(num)
    counter = int(0)
    if (num == 0):
        counter = int(1)
    else:
        while (num > 0):
            counter = int(counter + 1)
            num = int(num / 10)
    return counter

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n")
