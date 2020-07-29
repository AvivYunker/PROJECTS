import random
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

def digits_to_array (arr, num):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def random_binary_selector (arrNew, arrOrig):
    lim = len(arrOrig)
    for cnt in range(0, lim, 1):
        rndm = random.randrange(0, 2)
        arrNew.append(arrOrig[cnt] * rndm)

def array_to_number (num, arr):
    num = int(0)
    lim = len(arr)
    level = int(1)
    for cnt in range(lim-1, -1, -1):
        num = int(num + int(arr[cnt]) * level)
        level = int(level * 10)
    return num


x = input("User, enter a number:\n")
x = int(x)
arr_bin_orig = []
arr_bin_new = []
bin_orig = decimal_to_binary(x)
bin_select = int(0)
dec_select = int(0)
digits_to_array(arr_bin_orig, bin_orig)
random_binary_selector(arr_bin_new, arr_bin_orig)
bin_select = array_to_number(bin_select, arr_bin_new)
dec_select = int(binary_to_decimal(bin_select))

print("(DEC_ORIG: " + str(x), end=") / (BIN_ORIG: ")
print(str(bin_orig), end=") / (BIN_SELECT: ")
print(str(bin_select), end=") / (DEC_SELECT: ")
print(str(dec_select) + ")")
input("\nDONE!\n")
