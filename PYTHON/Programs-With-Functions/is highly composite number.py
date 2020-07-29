# CREATED BY: Aviv Yunker
# NAME: "is Highly-Composite number"
# TAGS: highly-composite, factor, if-else, while, if, function, return,
# EXPLANATION: This program will check if a number is highly composite.
# A highly composite numbers is a number that has more whole-divisors
# than any smaller integer of that number.
# EXAMPLE:
# 5 --> divisors are 1 --> 4 has more divisors than 5. 4 is NOT highly-composite.
# 6 --> divisors are 3,2,1 --> has more divisors than 5,4,3,2,1. 6 is highly-composite.
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


x = input("User, enter a number:\n")
x = int(x)
results = is_highly_composite(x)
if (results == 1):
    print(str(x) + " is a highly composite number:\n")
else:
    print(str(x) + " is NOT a highly composite number:\n")
input("\nDONE!\n") # This holds the CLI.
