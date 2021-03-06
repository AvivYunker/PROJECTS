import random
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
       digit_binary_boggled(lower)
       lower = int(lower + 1)

def digit_binary_boggled (num):
    num = int(num)
    arrDig = []
    arrBin = []
    arrNew = []
    print(str(num), end=" --> (")
    digits_to_array(num, arrDig)
    array_printer(arrDig)
    print(") --> (", end="")
    binary_rndm_to_array(arrDig, arrBin)
    array_printer(arrBin)
    print(") --> (", end="")
    binary_to_decimal_array(arrBin, arrNew)
    array_printer(arrNew)
    print(")")

def digits_to_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def binary_rndm_to_array (arrD, arrB):
    lim = len(arrD)
    level = int(1)
    temp = int(0)
    for cnt in range (0, lim, 1):
        while (arrD[cnt] > 0):
            rndm = random.randrange(0, 2)
            temp = int(temp + rndm * level)
            level = int(level * 10)
            arrD[cnt] = int(arrD[cnt] - 1)
        arrB.append(temp)
        level = int(1)
        temp = int(0)

def binary_to_decimal_array (arrB, arrN):
    lim = len(arrB)
    for cnt in range(0, lim, 1):
        temp = arrB[cnt]
        temp = binary_to_decimal(temp)
        arrN.append(temp)

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

def array_printer (arr):
    lim = len(arr)
    for cnt in range(lim-1, -1, -1):
        if (cnt == (0)):
            print(str(arr[cnt]), end="")
        else:
            print(str(arr[cnt]), end=",")

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n")
