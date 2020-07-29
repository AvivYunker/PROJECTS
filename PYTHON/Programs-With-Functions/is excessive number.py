# CREATED BY: Aviv Yunker
# NAME: "is excessive number"
# TAGS: excessive, if-else, function, return, while, modulus
# EXPLANATION: This program will receive a number, and will determine if the
# entered number is excessive or not. An excessive number is an integer that
# it's proper / whole divisors are greater than the original number
# EXAMPLE:
# 100 --> 50,25,20,10,5,4,2,1 --> 50+25+20+10+5+4+2+1 = 117. 117 > 100. 100 is excessive.
# 50 --> 25,10,5,2,1 --> 25+10+5+2+1 = 43. 43 < 50. 50 is NOT an excessive number
def is_excessive (num):
    num = int(num)
    factorSum = sum_all_factors(num)
    if (factorSum > num):
        return 1
    else:
        return 0

def sum_all_factors (num):
    num = int(num)
    b = int(num - 1)
    sumFactor = int(0)
    while (b > 0):
        if (num % b == 0):
            sumFactor = int(sumFactor + b)
        b = int(b - 1)
    return sumFactor


x = input("User, enter a number:  ")
x = int(x)
print("")
results = is_excessive(x)
if (results == 1):
    print(str(x) + " is an excessive number\n")
else:
    print(str(x) + " is NOT an excessive number\n")
input("\nDONE!\n") # This holds the CLI.
