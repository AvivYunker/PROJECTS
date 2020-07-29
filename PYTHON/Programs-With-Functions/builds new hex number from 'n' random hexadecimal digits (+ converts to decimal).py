# CREATED BY: Aviv Yunker
# NAME: "builds new hexadecimal number from 'n' random hexadecimals, then converts to decimal"
# TAGS: hexadecimal, conversion, random, decimal, while, if-elif, for-in, function, return, 
# EXPLANATION: if the input is 'n' (number), it will print 'n' random hexadecimal digits, form
# a hexadecimal number out of it, and reconvert to decimal
# EXAMPLE:
# 3 --> 5DE --> 1502
# 7 --> AB6221C --> 179708444

import random
def n_hexadecimal_digits (num, arr):
    num = int(num)
    newNum = int(0)
    while (num > 0):
        rndm = random.randrange(0, 16)
        if (rndm == 10):
            rndm = 'A'
        elif (rndm == 11):
            rndm = 'B'
        elif (rndm == 12):
            rndm = 'C'
        elif (rndm == 13):
            rndm = 'D'
        elif (rndm == 14):
            rndm = 'E'
        elif (rndm == 15):
            rndm = 'F'
        else:
            rndm = int(rndm)
        arr.append(rndm)
        #print(str(rndm), end=",")
        num = int(num - 1)
    newNum = build_hexadecimal(arr, newNum)
    return newNum

def build_hexadecimal (arr, res):
    res = ""
    lim = len(arr)
    for cnt in range (0, lim, 1):
        res += str((arr[cnt]));
    return res

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

x = input("User, how many random hexedecimal digits?\n")
x = int(x)
arr = []
y = n_hexadecimal_digits(x, arr)
print("\nThe new number is: " + str(y))
dec = hexadecimal_to_decimal(y)
print("The decimal equivalent of " + str(y) + " is: " + str(dec))
input("\nDONE!\n") # This holds the CLI.
