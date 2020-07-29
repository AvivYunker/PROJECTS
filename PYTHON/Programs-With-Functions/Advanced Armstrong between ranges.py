# CREATED BY: Aviv Yunker
# NAME: "Advanced Armstrong between ranges"
# TAGS: Armstrong, ranges, while, return, function, if, if-else, power, digit
# EXPLANATION: This program will print all the 'Advanced Armstrong' numbers in
# between the specified ranges. An 'Advanced Armstrong' number is one that
# has the following characteristics: the original number equals the sum of each
# of it's digits - in an incrementing power.
# EXAMPLE:
# 1 = 1^0 = 1. 1 == 1 --> is Advanced Armstrong
# 0 = 0^0 = 0. 0 == 0 --> is Advanced Armstrong
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        results = is_advanced_armstrong(lower)
        if (results == 1):
            print(str(lower) + " is an advanced Armstrong")
        lower = int(lower + 1)

def is_advanced_armstrong (num):
    num = int(num)
    orig = int(num)
    d = int(0)
    sums = int(0)
    while (num > 0):
        temp = int(num % 10)
        temp = int(pow(temp, d))
        sums = int(sums + temp)
        num = int(num / 10)
        d = int(d + 1)
    if (sums == orig):
        return 1
    else:
        return 0


lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n") # this holds the CLI
