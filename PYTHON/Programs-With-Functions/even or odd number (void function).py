# CREATED BY: Aviv Yunker
# NAME: "even or odd number"
# TAGS: even, odd, integer, input, output, no-return, print, function
# EXPLANATION: this program will receivea number - and will print whether the
# number is even or odd
# EXAMPLE:
# 13 - odd
# 14 - even
def even_or_odd (num):
    num = int(num)
    if (num % 2 == 0):
        print(str(num) + " is EVEN")
    else:
        print(str(num) + " is ODD")

x = input("User, enter a number:\n")
x = int(x)
even_or_odd(x)
input("\nDONE!\n") # This holds the CLI.
