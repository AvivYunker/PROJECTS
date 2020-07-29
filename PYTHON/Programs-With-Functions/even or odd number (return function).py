# CREATED BY: Aviv Yunker
# NAME: "even or odd number"
# TAGS: even, odd, return, function, if-else, input, output, modulus
# EXPLANATION: this program will receive an integer - and will print
# back - whether the number is even or odd
# EXAMPLE:
# input 12 - even
# input 13 - odd
def even_or_odd (num):
    num = int(num)
    if (num % 2 == 0):
        return 1
    else:
        return 0

x = input("User, enter a number:\n")
x = int(x)

results = even_or_odd(x)

if (results == 1):
    print(str(x) + " is EVEN")
else:
    print(str(x) + " is ODD")
input("\nDONE!\n") # This holds the CLI.
