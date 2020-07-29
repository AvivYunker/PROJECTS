# CREATED BY: Aviv Yunker
# NAME: "Highly-Composite numbers between ranges"
# TAGS: highly-composite, factor, if-else, while, if, function, return,
# EXPLANATION: This program will print all highly-composite numbers in
# between ranges. A highly composite numbers is a number that has more whole-divisors
# than any smaller integer of that number.
# EXAMPLE:
# 5 --> divisors are 1 --> 4 has more divisors than 5. 4 is NOT highly-composite.
# 6 --> divisors are 3,2,1 --> has more divisors than 5,4,3,2,1. 6 is highly-composite.
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        results = is_highly_composite(lower)
        if (results == 1):
            print(str(lower) + " is highly-composite")
        lower = int(lower + 1)

def is_highly_composite (num):
    num = int(num)
    fcNum = factor_counter(num) #where 'f' means 'factor' and 'c' means 'count'
    b = int(num - 1)
    while (b > 0):
        fcB = factor_counter(b)
        if (fcB >= fcNum):
            return 0
        else:
            b = int(b - 1)
    return 1

def factor_counter (num):
    num = int(num)
    b = int(num - 1)
    counter = int(0)
    while (b > 0):
        if (num % b == 0):
            counter = int(counter + 1)
        b = int(b - 1)
    return counter


lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n") # This holds the CLI.
