# CREATED BY: Aviv Yunker
# NAME: "Hexadecimal taxer for all decimals between ranges"
# TAGS: hexadecimal, decimal, taxer, random, if-elif, while, if, for-in, function, return, print
# EXPLANATION: for every decimal number between ranges - a random hexadecimal digit will be
# selected - and then the original decimal number will be subtracted from that
# randomly selected value.
# EXAMPLE:
# 50 --> 6,3,F,6,C,8
# 100 --> 7,D,4,5,9,9,5,8,1,3,6,E,4,C
import random
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        print(str(lower), end=": (")
        hex_taxer(lower)
        print(")")
        lower = int(lower + 1)

def hex_taxer (num):
    num = int(num)
    while (num >= 1):
        tax = random.randrange(0, 16)
        if (num >= tax):
            num = int(num - tax)
            tax = decimal_to_hexadecimal(tax)
            print(str(tax), end=",")

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

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n") # This holds the CLI.
