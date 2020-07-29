# CREATED BY: Aviv Yunker
# NAME: "excessive numbers between ranges"
# TAGS: excessive, while, if-else, return, ranges, print
# EXPLANATION: this program will print all the excessive numbers
# between the assigned ranges. An excessive number is a number
# that the sum of it's divisors are larger than the number itself
# EXAMPLE:
# 100 - divisors are: 50,25,20,10,5,4,2,1 --> sum is 117 --> 117 > 100 - is excessive
# 10 - divisors are: 5,2,1 --> sum is 8 --> 10 > 8 - is NOT excessive
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        results = is_excessive(lower)
        if (results == 1):
            print(str(lower) + " is an excessive number")
        lower = int(lower + 1)

def is_excessive (num):
    num = int(num)
    factorSum = sum_all_factors(num)
    if (factorSum > num):
        return 1
    else:
        return 0

def sum_all_factors (num):
    num = int(num)
    b = int(num - 1)
    sumFactor = int(0)
    while (b > 0):
        if (num % b == 0):
            sumFactor = int(sumFactor + b)
        b = int(b - 1)
    return sumFactor


lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n") # This holds the CLI.
