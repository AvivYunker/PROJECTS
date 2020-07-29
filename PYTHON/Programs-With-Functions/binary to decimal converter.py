# CREATED BY: Aviv Yunker
# NAME: "binary to decimal converter"
# TAGS: binary, decimal, conversion, while, return, function, input, output,
# EXPLANATION: This program will take the entered binary number, and convert
# it into a decimal number
# EXAMPLE:
# 111 --> 7
# 10010 --> 18

def binary_to_decimal (num):
    num = int(num);
    sums = int(0);
    level = int(0);
    while (num > 0):
        temp = int(num % 10);
        temp = int(temp * pow(2,level));
        sums = int(sums + temp);
        level = int(level + 1);
        num = int(num / 10);
    return sums;

x= input("User, enter a binary number:\n");
x = int(x);

results = binary_to_decimal(x);
print("The decimal equivalent is: " + str(results));
input("\nDONE!\n"); # This holds the CLI.
