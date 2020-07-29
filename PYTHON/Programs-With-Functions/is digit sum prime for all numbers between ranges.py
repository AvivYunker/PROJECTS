# CREATED BY: Aviv Yunker
# CREATED BY: Aviv Yunker
# NAME: is sum of digits a prime number, between ranges
# TAGS: sum, digits, prime, ranges, function, return, while, if, 
# EXPLANATION: This program will receive an integer - sum the digits of this
# integer - and then will check whther this sum is a prime number or not (this
# time it will go for each decimal between ranges).
# EXAMPLE:
# 123 --> 1 + 2 + 3 = 6. 6 is NOT a prime number.
# 779 --> 7 + 7 + 9 = 23. 23 is a prime number.
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        sum_digits = digit_sum(lower)
        results = is_prime(sum_digits)
        if (results == 1):
            print("(" + str(lower) + ") --> (SUM_DIGITS:" + str(sum_digits) + ") --> (IS PRIME)")
        lower = int(lower + 1)

def digit_sum (num):
    num = int(num)
    sums = int(0)
    while (num > 0):
        temp = int(num % 10)
        sums = int(sums + temp)
        num = int(num / 10)
    return sums

def is_prime (num):
    num = int(num)
    b = int(num - 1)
    while (b > 1):
        if (num % b == 0):
            return 0
        b = int(b - 1)
    return 1

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n") # This holds the CLI.
