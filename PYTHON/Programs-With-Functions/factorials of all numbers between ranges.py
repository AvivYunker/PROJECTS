# CREATED BY: Aviv Yunker
# NAME: "factorial of all numbers between ranges"
# TAGS: factorial, ranges, function, return, math, print,
# EXPLANATION: this program will print (for every number in between the
# specified ranges) the factorial of the single number.
# EXAMPLE:
# input: 5 - results: 120
# input: 6 - results: 720

def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        print(str(lower), end=" --> )")
        results = factorial(lower)
        print(str(results) + ")")
        lower = int(lower + 1)

def factorial(num):
    num = int(num)
    res = int(1)
    while (num > 0):
        res = int(res * num)
        num = int(num - 1)
    return res

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n") # This holds the CLI.
