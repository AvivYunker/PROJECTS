# (1234) --> (4D2) --> (1010, 1111000111011, 10) --> (10, 7739, 2)
import random
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

def insert_into_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def digits_to_array (num, arr):
    lim = len(num)
    for cnt in range(0, lim, 1):
        arr.append(num[cnt])

def hex_boggled_binary (arrH, arrB):
    limH = len(arrH)
    for cnt in range(0, limH, 1):
        val = hex_to_num(arrH[cnt])
        tempB = int(0)
        level = int(1)
        while (val > 0):
            rndm = random.randrange(0, 2)
            tempB = int(tempB + level*rndm)
            level = int(level * 10)
            val = int(val - 1)
        arrB.append(tempB)


def hex_to_num (num):
    num = str(num)
    res = int(0)
    if (num == 'A'):
        res = int(10)
    elif (num == 'B'):
        res = int(11)
    elif (num == 'C'):
        res = int(12)
    elif (num == 'D'):
        res = int(13)
    elif (num == 'E'):
        res = int(14)
    elif (num == 'F'):
        res = int(15)
    else:
        res = int(num)
    return res

def binary_to_decimal_array(arrB, arrD):
    limB = len(arrB)
    for cnt in range(0, limB, 1):
        val = binary_to_decimal(arrB[cnt])
        arrD.append(val)

def binary_to_decimal (num):
    num = int(num);
    sum = int(0);
    level = int(0);
    while (num > 0):
        temp = int(num % 10);
        temp = int(temp * pow(2,level));
        sum = int(sum + temp);
        level = int(level + 1);
        num = int(num / 10);
    return sum;

def print_array_contents(arr):
    lim = len(arr)
    for cnt in range(0, lim, 1):
        if (cnt == (lim-1)):
            print(str(arr[cnt]), end="")
        else:
            print(str(arr[cnt]), end=",")

x = input("User, enter a number:\n")
arrBin = []
arrHex = []
arrDec = []
decOrig = int(x)
print("(" + str(decOrig), end=") --> (")
hexOrig = decimal_to_hexadecimal(decOrig)
print(str(hexOrig), end=") --> (")
digits_to_array(hexOrig, arrHex)
hex_boggled_binary(arrHex, arrBin)
print_array_contents(arrBin)
print(") --> (", end="")
binary_to_decimal_array(arrBin, arrDec)
print_array_contents(arrDec)
print(")")
input("\nDONE!\n")