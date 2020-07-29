# CREATED BY: Aviv Yunker
# NAME: "binary produced of digit-sum of decimal number, between ranges"
# TAGS: binary, random, decimal, convert, while, return, function, ranges
# EXPLANATION: This will take a single decimal number (in between the ranges),
# sum the digits, and according to the sum of digits - will assign a random binary number
# print it, and then convert it back to decimal.
# EXAMPLE:
# 1234 --> has 10 digits --> 1111001100 is a random binary number --> 972 is the conversion back to decimal
import random
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        print("(" + str(lower), end=") --> (")
        sum_d = digit_counter(lower)
        print(str(sum_d), end = ") --> (")
        num_bin = randomized_binary_by_digits(sum_d)
        print(str(num_bin), end = ") --> (")
        dec_cnvt = binary_to_decimal(num_bin)
        print(str(dec_cnvt) + ")")
        lower = int(lower + 1)

def digit_counter (num):
    num = int(num)
    res = int(0)
    while (num > 0):
        temp = int(num % 10)
        res = int(res + temp)
        num = int(num / 10)
    return res

def randomized_binary_by_digits (dig_select):
    dig_select = int(dig_select)
    res = int(0)
    level = int(1)
    while (dig_select > 0):
        rndm = random.randrange(0, 2)
        temp = int(rndm * level)
        res = int(res + temp)
        level = int(level * 10)
        dig_select = int(dig_select - 1)
    return res

def binary_to_decimal (num):
    num = int(num);
    sum = int(0);
    level = int(0);
    while (num > 0):
        temp = int(num % 10);
        temp = int(temp * pow(2,level));
        sum = int(sum + temp);
        level = int(level + 1);
        num = int(num / 10);
    return sum;

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n") # This holds the CLI.
