def decimal_to_binary (num):
    num = int(num)
    res = int(0)
    level = int(1)
    while (num > 0):
        tempI = int(num / 2)
        tempF = float(num*1.0 / 2)
        tempF = float(tempF - tempI)
        tempF = int(tempF * 2)
        res = int(res + level * tempF)
        level = int(level * 10)
        num = int(tempI)
    return res

def binary_reverser (num):
    num = int(num)
    res = int(0)
    arrOrig = []
    arrNew = []
    digits_to_array(arrOrig, num)
    assign_array_reverser(arrNew, arrOrig)
    res = array_to_number(res, arrNew)
    return res

def digits_to_array (arr, num):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def assign_array_reverser(arrN, arrO):
    lim = len(arrO)
    for cnt in range(lim-1, -1, -1):
        arrN.append(arrO[cnt])

def array_to_number (num, arr):
    lim = len(arr)
    res = int(0)
    level = int(1)
    for cnt in range(0, lim, 1):
        res = int(res + level * arr[cnt])
        level = int(level * 10)
    return res

def binary_to_decimal (num):
    num = int(num)
    level = int(0)
    res = int(0)
    while (num > 0):
        temp = int(num % 10)
        temp = int(temp * pow(2, level))
        res = int(res + temp)
        level = int(level + 1)
        num = int(num / 10)
    return res

x = input("User, enter a number:\n")
dec_orig = int(x)
bin_orig = decimal_to_binary(dec_orig)
bin_rev = binary_reverser(bin_orig)
dec_rev = binary_to_decimal(bin_rev)

print("\n")
print(str(dec_orig))
print(str(bin_orig))
print(str(bin_rev))
print(str(dec_rev))

input("\nDONE!\n")

