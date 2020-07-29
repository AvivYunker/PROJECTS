# CREATED BY: Aviv Yunker
# NAME: "Hexadecimal boggler for all decimals between ranges"
# TAGS: hexadecimal, decimal, ranges, boggled, boggler, function, return, while, if-elif, for-in, char
# EXPLANATION: for each decimal number in between ranges - it will print the decimal number,
# the hexadecimal equivalent, the boggled hexadecimal, and the recoversion of the boggled hexadecimal
# to the decimal equivalent.
# EXAMPLE:
# 1000 --> 3E8 --> 38E --> 910
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        print("ORIG_DEC(" + str(lower), end=") --> ")
        hex_orig = decimal_to_hexadecimal(lower)
        print("ORIG_HEX(" + str(hex_orig), end=") --> ")
        hex_bogg = hexadecimal_boggler(hex_orig)
        print("BOGG_HEX(" + str(hex_bogg), end=") --> ")
        dec_bogg = hexadecimal_to_decimal(hex_bogg)
        print("BOGG_DEC(" + str(dec_bogg) + ")")
        lower = int(lower + 1)

import random
def hexadecimal_boggler (num):
    arr = []
    res = str('')
    digits_to_array(num, arr)
    res = boggler(arr, res)
    return res

def digits_to_array (num, arr):
    lim = len(num)
    for cnt in range(0, lim, 1):
        arr.append(num[cnt])

def boggler(arr, res):
    lim = len(arr)
    d = are_all_zero(arr)
    while (d == 0):
        rndm = random.randrange(0, lim)
        if (arr[rndm] != int(-1)):
            res += arr[rndm]
            arr[rndm] = int(-1)
        d = are_all_zero(arr)
    return res


def are_all_zero(arr):
    lim = len(arr)
    sums = int(0)
    for cnt in range(0, lim, 1):
        if (arr[cnt] != -1):
            return 0
    return 1

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

def hexadecimal_to_decimal (num):
    num = str(num);
    lim = len(num);
    level = int(0);
    res = int(0);
    arr = [];
    for cnt1 in range (0, lim, 1):
        arr.append(num[cnt1]);

    for cnt2 in range (lim - 1, -1, -1):
        if (arr[cnt2] == 'A' or arr[cnt2] == 'a'):
            temp = int(10);
        elif(arr[cnt2] == 'B' or arr[cnt2] == 'b'):
            temp = int(11);
        elif(arr[cnt2] == 'C' or arr[cnt2] == 'c'):
            temp = int(12);
        elif(arr[cnt2] == 'D' or arr[cnt2] == 'd'):
            temp = int(13);
        elif(arr[cnt2] == 'E' or arr[cnt2] == 'e'):
            temp = int(14);
        elif(arr[cnt2] == 'F' or arr[cnt2] == 'f'):
            temp = int(15);
        elif (int(arr[cnt2]) >= 0 and int(arr[cnt2]) <= 9):
            temp = int(arr[cnt2]);
        else:
            print("ERROR! not a hexadecimal number!");
            return 0;
        res = int(res + temp * pow(16, level));
        level = int(level + 1);

    return res;


lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n") # This holds the CLI.
