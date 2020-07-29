# CREATED BY: Aviv Yunker
# NAME: "is the sum of digits a prime number"
# TAGS: digits, prime, sum, function, return, while, if, if-else
# EXPLANATION: this program will receive a number, and will check of the sum
# of digits of the entered number is a prime number or not.
# EXAMPLE:
# entered 995 --> digit sum 23 --> 23 is a prime number.
# entered 255 --> digit sum 12 --> 12 is NOT a prime number.
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

x = input("User, enter a number:\n")
x = int(x)
dig_sum = digit_sum(x)
results = is_prime(dig_sum)
if (results == 1):
    print(str(x) + " has digit sum of " + str(dig_sum) + " and is prime")
else:
    print(str(x) + " has digit sum of " + str(dig_sum) + " and is NOT prime")
input("\nDONE!\n") # This holds the CLI
