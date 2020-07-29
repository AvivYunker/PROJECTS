# CREATED BY: Aviv Yunker
# NAME: decimal to binary converter
# TAGS: decimal, binary, conversion, return, while, function, input, ouput
# EXPLANATION: this program will receive a decimal number - and will convert
# it inot a binary number
# EXAMPLE:
# 15 --> 1111
# 18 --> 10010
# 7 --> 111
def decimal_to_binary (num):
    num = int(num);
    sum = int(0);
    pusher = int(1);
    while (num > 0):
        temp = int(num % 2);
        sum = int(sum + temp * pusher);
        num = int(num / 2);
        pusher = int(pusher * 10);
    return sum;


x = input("User, enter a decimal number:\n");
x = int(x);

results = decimal_to_binary(x);
print("The binary equivalent is: " + str(results));
input("\nDONE!\n"); # This holds the CLI.
