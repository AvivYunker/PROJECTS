# CREATED BY: Aviv Yunker
# NAME: decimal + binary + octal + hexadecimal conversions between ranges
# TAGS: decimal, binary, octal, hexadecimal conversion, ranges, function, return, ranges, while, if-elif, print
# EXPLANATION: for each number in between ranges - it will print the decimal, binary, octal and hexadecimal equivalents.
# EXAMPLE:
# 15 (decimal) --> 1111 (binary) --> 17 (octal) --> A (hexadecimal)
def between_ranges (lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        print("/DEC:" + str(lower) + "/BIN:" + str(decimal_to_binary(lower)) + "/OCT:" + str(decimal_to_octal(lower)) + "/HEX:" + decimal_to_hexadecimal(lower));
        lower = int(lower + 1);
    print("DONE!\n");

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


lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
input("\nDONE!\n"); # This holds the CLI.
