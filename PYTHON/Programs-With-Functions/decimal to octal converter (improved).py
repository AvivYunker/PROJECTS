# CREATED BY: Aviv Yunker
# NAME: decimal to octal converter
# TAGS: decimal, octal, conversion, while, integer, float, return, function
# EXPLANATION: this program will receive a decimal number, and will return the octal
# equivalent of the entered decimal number
# EXAMPLE:
# 1499 --> 2733
# 3900 --> 7474
def decimal_to_octal (num):
    num = int(num);
    sums = int(0);
    level = int(1);
    while (num > 0):
        tempI = int(num / 8);
        tempF = float(num*1.0 / 8);
        tempF = float(tempF - tempI);
        tempF = int(tempF * 8);
        tempF = int(tempF * level);
        sums = int(sums + tempF);
        level = int(level * 10);
        num = int(tempI);
    return sums;


x = input("User, enter a decimal number:\n");
x = int(x);
results = decimal_to_octal(x);
print("The octal equivalent is: " + str(results));
input("\nDONE!\n"); # This holds the CLI.
