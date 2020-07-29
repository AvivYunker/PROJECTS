# CREATED BY: Aviv Yunker
# NAME: "Amicable numbers between ranges"
# TAGS: Amicable, ranges, while, if, modulus, even, no-return
# EXPLANATION: This program wll print all the pairs of numbers that
# are amicable numbers. Amicable numbers are pairs of numbers that the sum of
# all proper divisors equal to the other number.
# EXAMPLE:
# 220 and 284
# 220 --> 1+2+4+5+10+11+20+22+44+55+110 = 284
# 284 --> 1+2+4+71+142 = 220
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        is_amicable(lower)
        lower = int(lower + 1)

def is_amicable (num):
    num = int(num)
    b = int(num - 1)
    sumDiv = int(0)
    sumDiv2 = int(0)
    while (b > 0):
        if (num % b == 0):
            sumDiv = int(sumDiv + b)
        b = int(b - 1)
    b = int(sumDiv - 1)
    while (b > 0):
        if (sumDiv % b == 0):
            sumDiv2 = int(sumDiv2 + b)
        b = int(b - 1)
    if (sumDiv2 == num):
        print(str(num) + " and " + str(sumDiv))

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n") # this holds the CLI
