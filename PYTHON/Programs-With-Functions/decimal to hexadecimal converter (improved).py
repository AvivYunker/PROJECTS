# CREATED BY: Aviv Yunker
# NAME: "decimal to hexadecimal converter"
# TAGS: decimal, hexadecimal, converted, while, if-elif, for-in, return, if, input, output, list, length
# EXPLANATION: this program will receive a decimal number - and will convert it into a
# hexadecimal number
# EXAMPLE:
# 15 --> F
# 9550 --> 254E

def decimal_to_hexadecimal (num):
    num = int(num);
    arr = [];
    if (num == 0):
        arr.append(0);
    while (num > 0):
        tempF = float(num / 16);
        tempI = int(num / 16);
        tempF = float(tempF - tempI);
        tempF = int(tempF * 16);
        if (tempF == 10):
            tempF = 'A';
        elif (tempF == 11):
            tempF = 'B';
        elif (tempF == 12):
            tempF = 'C';
        elif (tempF == 13):
            tempF = 'D';
        elif (tempF == 14):
            tempF = 'E';
        elif (tempF == 15):
            tempF = 'F';
        elif (tempF >= 0 and tempF <= 9):
            tempF = int(tempF);
        arr.append(tempF);
        num = int(tempI);
    res = "";
    lim = len(arr);
    for cnt in range(lim - 1, -1, -1):
        res += str((arr[cnt]));
    return res;

x = input("User, enter decimal number:\n");
x = int(x);
results = decimal_to_hexadecimal(x);
print("The hexadecimal equivalent is:\n" + str(results));
input("\nDONE!\n"); # This holds the CLI.
