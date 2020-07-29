# CREATED BY: Aviv Yunker
# NAME: Boggled hexadecimal of single number
# TAGS: boggled, hexadecimal, return, for-in, while, if, return, function,
# EXPLANATION: This program will take the original decimal number that had been entered
# and will convert it into a hexadecimal number. Then - it will boggle that hexadecimal number
# and print that number. Finally - it will convert that hexadecimal number back to decimal - and
# will print that number.
# EXMAPLE:
# 1234 --> 4D2 (hexadecimal equivalent) --> 24D (boggled hexadecimal) --> 589 (reconverted decimal)
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


dec_orig = input("User, enter a decimal number:\n")
dec_orig = int(dec_orig)
print("original decimal is: " + str(dec_orig))
hex_orig = decimal_to_hexadecimal(dec_orig)
print("original hexadecimal is: " + str(hex_orig))
hex_bogg = hexadecimal_boggler(hex_orig)
print("boggled hexadecimal is: " + str(hex_bogg))
dec_bogg = hexadecimal_to_decimal(hex_bogg)
print("boggled decimal is: " + str(dec_bogg))
input("\nDONE!\n") # This holds the CLI.
