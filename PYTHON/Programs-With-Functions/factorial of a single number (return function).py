# CREATED BY: Aviv Yunker
# NAME: "factorial"
# TAGS: factorial, numeric, math, while, return, function, print, factor
# EXPLANATION: this program will return the factor of a given number.
# EXAMPLE:
# input: 5 --> 5*4*3*2*1 = 120
def factorial (num):
    num = int(num)
    res = int(1)
    while (num > 0):
        res = int(res * num)
        num = int(num - 1)
    return res

x = input("User, enter a number:\n")
x = int(x)
results = factorial(x)
print("the factorial of " + str(x) + " is: " + str(results))
input("\nDONE!\n") # This holds the CLI.
