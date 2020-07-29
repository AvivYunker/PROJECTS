import random
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

x = input("User, enter a decimal number:\n")
x = int(x)
print("Original decimal: " + str(x))
oct_orig = decimal_to_octal(x)
print("Original octal: " + str(oct_orig))
oct_bogg = octal_boggler(oct_orig)
print("Boggled octal: " + str(oct_bogg))
dec_bogg = octal_to_decimal(oct_bogg)
print("Boggled decimal: " + str(dec_bogg))
input("\nDONE!\n")