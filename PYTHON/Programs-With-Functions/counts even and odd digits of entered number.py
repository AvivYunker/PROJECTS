# CREATED BY: Aviv Yunker
# NAME: "counts even and odd digits in a single number"
# TAGS: even, odd, digits, print, no-return, function, modulus
# EXPLANATION: this program will receive a number - and count the number of even / odd digits that the number contains.
# EXAMPLE:
# 12345 --> 2 even-digits / 3 odd-digits
def even_odd_counter (num):
    num = int(num)
    cntE = int(0)
    cntO = int(0)
    while (num > 0):
        temp = int(num % 10)
        if (temp % 2 == 0):
            cntE = int(cntE + 1)
        else:
            cntO = int(cntO + 1)
        num = int(num / 10)
    print("Count of even digits is: " + str(cntE))
    print("Count of odd digits is: " + str(cntO))


x = input("User, enter a number:\n")
x = int(x)

even_odd_counter(x)
input("\nDONE!\n") # This holds the CLI.
