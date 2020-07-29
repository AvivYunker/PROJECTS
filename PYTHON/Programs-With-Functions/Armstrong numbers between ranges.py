# CREATED BY: Aviv Yunker
# NAME: Armstrong numbers between ranges
# TAGS: Armstrong, ranges, function, return, while, if, if-else, modulus, digit-counter
# EXPLANATION: this program will print all Armstrong numbers in between ranges.
# An Armstrong number is a number that has the following properties: take each of it's
# digits - power them by the total number of digits, sum everything - and if the sum equals
# to the original number - then it's an Armstrong.
# EXAMPLE:
# 110 --> 1^3 + 1^3 + 0^3 = 2. 2 != 100 --> NOT an Armstrong.
# 407 --> 4^3 + 0^3 + 7^3 = 64 + 343 = 407 --> 407 == 407 --> is an Armstrong.
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        results = is_armstrong(lower)
        if (results == 1):
            print(str(lower) + " is an Armstrong")
        lower = int(lower + 1)

def is_armstrong (num):
    num = int(num)
    orig = int(num)
    d = digit_counter(num)
    sums = int(0)
    while (num > 0):
        temp = int(num % 10)
        temp = pow(temp, d)
        sums = int(sums + temp)
        num = int(num / 10)
    if (sums == orig):
        return 1
    else:
        return 0

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
input("\nDONE!\n") # This holds the CLI.
