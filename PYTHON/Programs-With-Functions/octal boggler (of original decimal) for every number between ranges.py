import random
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        print("DEC_ORIG: " + str(lower), end=" --> (")
        oct_orig = int(decimal_to_octal(lower))
        print("OCT_ORIG: " + str(oct_orig), end=") --> (")
        oct_bogg = int(octal_boggler(oct_orig))
        print("OCT_BOGG: " + str(oct_bogg), end=") --> (")
        dec_bogg = octal_to_decimal(oct_bogg)
        print("DEC_BOGG: " + str(dec_bogg) + ")")
        lower = int(lower + 1)

def decimal_to_octal (num):
    num = int(num)
    res = int(0)
    level = int(1)
    while (num > 0):
        tempI = int(num / 8)
        tempF = float(num*1.0 / 8)
        tempF = float(tempF - tempI)
        tempF = int(tempF * 8)
        res = int(res + level * tempF)
        level = int(level * 10)
        num = int(tempI)
    return res

def octal_boggler(num):
    num = int(num)
    arr = []
    res = int(0)
    digits_to_array(num, arr)
    res = boggler(arr, res)
    return res

def digits_to_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def boggler (arr, newNum):
    newNum = int(0)
    lim = len(arr)
    level = int(1)
    d = all_minus(arr)
    while (d == 0):
        rndm = random.randrange(0, lim)
        if (arr[rndm] != int(-1)):
            newNum = int(newNum + level * arr[rndm])
            #print(str(newNum))
            arr[rndm] = int(-1)
            level = int(level * 10)
        d = all_minus(arr)
    return newNum

def all_minus (arr):
    lim = len(arr)
    for cnt in range(0, lim, 1):
        if (arr[cnt] != -1):
            return 0
    return 1

def octal_to_decimal (num):
    num = int(num)
    level = int(0)
    res = int(0)
    while (num > 0):
        temp = int(pow(8, level))
        temp = int((num % 10) * temp)
        res = int(res + temp)
        level = int(level + 1)
        num = int(num / 10)
    return res

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n")
