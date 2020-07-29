# CREATED BY: Aviv Yunker
# NAME: "decimal to binary converter"
# TAGS: decimal, binary, conversion, convert, while, return, function, input, output, integer, float,
# EXPLANATION: this program will receive a decimal number - and return the binary equivalent.
# EXAMPLE:
# entered 7 - ouput: 111
# entered 18 - output: 10010

def decimal_to_binary (num):
    num = int(num);
    sums = int(0);
    level = int(1);
    while (num > 0):
        tempI = int(num / 2);
        tempF = float(num*1.0 / 2);
        tempF = float(tempF - tempI);
        tempF = int(tempF * 2);
        tempF = int(tempF * level);
        sums = int(sums + tempF);
        level = int(level * 10);
        num = int(tempI);
    return sums;


x = input("User, enter a decimal number:\n");
x = int(x);
results = decimal_to_binary(x);
print("The binary equivalent is: " + str(results));
input("DONE!"); # This holds the CLI.
