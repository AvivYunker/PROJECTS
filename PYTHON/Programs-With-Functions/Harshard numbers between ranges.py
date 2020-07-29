# CREATED BY: Aviv Yunker
# NAME: "Harshard numbers between ranges"
# TAGS: harshard, ranges, if-else, return, for-in, while, function
# EXPLANATION: This program will print all Harshard numbers in between ranges
# a hardshard number is an integer - that can be divided by the sum of it's digits
# EXAMPLE:
# 12 --> divisors are: 6,3,2,1 --> 6+3+2+1 = 12. 12 can be divided by 12.

def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        results = is_harshard(lower)
        if (results == 1):
            print(str(lower) + " is Harshard")
        lower = int(lower + 1)

def is_harshard (num):
    num = int(num)
    arr = []
    digits_to_array(num, arr)
    sumD = digit_summer(arr)
    if (sumD == 0):
        return 0
    else:
        if (num % sumD == 0):
            return 1
        else:
            return 0

def digits_to_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def digit_summer(arr):
    res = int(0)
    lim = len(arr)
    for cnt in range(0, lim, 1):
        res = int(res + arr[cnt])
    return res

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n") # This holds the CLI.
