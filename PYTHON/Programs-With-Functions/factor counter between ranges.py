# CREATED BY: Aviv Yunker
# NAME: "factor counter between ranges"
# TAGS: factor, counter, ranges, while, functions, return, print, if
# EXPLANATION: this program will print the number of factors of each number
# between the specified ranges. A pair of factors of a number are the numbers
# that can get multiplied by each other in order to receive the original number
# EXAMPLE:
# input 12 - (6,2), (3,4), (12,1) - 3 pairs = 6 factors
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        print(str(lower), end=" --> (")
        count = factor_counter(lower)
        print("has " + str(count) + " factors)")
        lower = int(lower + 1)

def factor_counter (num):
    num = int(num)
    b = int(num)
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
