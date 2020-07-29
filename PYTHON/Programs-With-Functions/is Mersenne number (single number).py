# CREATED BY: Aviv Yunker
# NAME: "is Mersenne number"
# TAGS: Mersenne, numeric, input, ouput, function, return, print, while, if
# EXPLANATION: This program will receive a single number - and determine whether
# or not the number is Mersenne. A Mersenne number is a number that forms a prime
# number from the equasion:'2^n - 1'. If 'n' produces a prime number - then 'n'
# is a Mersenne number.
# EXAMPLE:
# input 13.
# 2^13 - 1 = 8191. 8191 is a prime number. Therefore - 13 is Mersenne.
# input 5.
# 2^6 - 1 = 63. 63 is NOT a prime number. Therefore - 6 is NOT Mersenne.
def is_mersenne(num):
    num = int(num + 1)
    res = is_two_power(num)
    return res

def is_two_power(num):
    while num > 2:
        num = int(num / 2)
        if num == 2:
            return 1
    return 0


x = input("User, enter a number:\n")
x = int(x)

results = is_mersenne(x)
if results == 1:
    print(str(x) + " is Mersenne")
else:
    print(str(x) + " is NOT mersenne")
input("\nDONE!\n") # This holds the CLI.
