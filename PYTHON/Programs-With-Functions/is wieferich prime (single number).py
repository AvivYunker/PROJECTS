# CREATED BY: Aviv Yunker
# NAME: "is wieferich prime"
# TAGS: Wieferich, numeric, prime, function, return, while, if, if-else, print
# EXPLANATION: This program receives a number, and determines whether this number
# is Wieferich or not. A Wieferich number is a number that has the following
# property:
# input: x
# expression_1 = x^2
# expression_2 = 2^(x-1) - 1
# if expression_1 % expression_2 == 0 --> then wieferich number
# EXAMPLE:
def is_wieferich_prime (num):
    num = int(num)
    res1 = is_prime(num)
    if (res1 == 1):
        res2 = is_wieferich(num)
        if (res2 == 1):
            return 1
        else:
            return 0
    else:
        return 0

def is_prime (num):
    num = int(num);
    b = int(num - 1);
    while (b > 1):
        if (num % b == 0):
            return 0;
        b = int(b - 1);
    return 1;

def is_wieferich (num):
    num = int(num)
    num1 = int(pow(num, 2))
    num2 = int(pow(2, (num-1)) - 1)
    if (num2 % num1 == 0):
        return 1
    else:
        return 0

x = input("User, enter a number:\n")
x = int(x)
results = is_wieferich_prime(x)
if (results == 1):
    print(str(x) + " is a Wieferich prime")
else:
    print(str(x) + " is NOT a Wieferich prime")
input("\nDONE!\n")
