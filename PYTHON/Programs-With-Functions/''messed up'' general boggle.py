import random
def characters_to_array (arr, strr):
    strr = str(strr)
    lim = len(strr)
    for cnt in range(0, lim, 1):
        arr.append(strr[cnt])

def digits_to_array (arr, num):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

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

def decimal_to_octal (num):
    num = int(num)
    level = int(1)
    res = int(0)
    while (num > 0):
        tempI = int(num / 8)
        tempF = float(num * 1.0 / 8)
        tempF = float(tempF - tempI)
        tempF = int (tempF * 8)
        res = int(res + tempF * level)
        level = int(level * 10)
        num = int(tempI)
    return res

def decimal_to_hexadecimal (num):
    num = int(num)
    arr = []
    res = ""
    while (num > 0):
        tempI = int(num / 16)
        tempF = float(num * 1.0 / 16)
        tempF = float(tempF - tempI)
        tempF = int(tempF * 16)
        if (tempF >= 10 and tempF <= 15):
            tempF = int(tempF + 55)
            arr.append(chr(tempF))
        else:
            tempF = int(tempF)
            arr.append(tempF)
        num = int(tempI)
    lim = len(arr)
    for cnt in range(lim-1, -1, -1):
        res += str(arr[cnt])
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

def octal_to_decimal (num):
    num = int(num)
    res = int(0)
    level = int(0)
    while (num > 0):
        temp = int(num % 10)
        temp = int(temp * pow(8, level))
        res = int(res + temp)
        level = int(level + 1)
        num = int(num / 10)
    return res

def hexadecimal_to_decimal (num):
    num = str(num)
    lim = len(num)
    level = int(0)
    res = int(0)
    for cnt in range(lim-1, -1, -1):
        if (num[cnt] == 'A' or num[cnt] == 'a'):
            res = int(res + 10 * pow(16, level))
        elif (num[cnt] == 'B' or num[cnt] == 'b'):
            res = int(res + 11 * pow(16, level))
        elif (num[cnt] == 'C' or num[cnt] == 'c'):
            res = int(res + 12 * pow(16, level))
        elif (num[cnt] == 'D' or num[cnt] == 'd'):
            res = int(res + 13 * pow(16, level))
        elif (num[cnt] == 'E' or num[cnt] == 'e'):
            res = int(res + 14 * pow(16, level))
        elif (num[cnt] == 'F' or num[cnt] == 'f'):
            res = int(res + 15 * pow(16, level))
        else:
            res = int(res + int(num[cnt]) * pow(16, level))
        level = int(level + 1)
    return res

def rndm_string_array (strr, arr):
    lim = len(arr)
    d = all_minus(arr)
    while (d == 0):
        rndm = random.randrange(0, lim)
        if (arr[rndm] != int(-1)):
            strr += str(arr[rndm])
            arr[rndm] = int(-1)
            d = all_minus(arr)
    return strr

def all_minus (arr):
    lim = len(arr)
    for cnt in range(0, lim, 1):
        if (arr[cnt] != int(-1)):
            return 0
    return 1

def random_conversion_checker (strr):
    strr = str(strr)
    d = int(0)
    res = int(0)
    while (d == 0):
        rndm = random.randrange(0, 3)
        if (rndm == 0):
            d = is_bin_valid(strr)
            if (d == 1):
                res = binary_to_decimal(strr)
        elif (rndm == 1):
            d = is_oct_valid(strr)
            if (d == 1):
                res = octal_to_decimal(strr)
        elif (rndm == 2):
            d = is_hex_valid(strr)
            if (d == 1):
                res = hexadecimal_to_decimal(strr)
    return res

def is_bin_valid (num):
    num = str(num)
    lim = len(num)
    for cnt in range(0, lim, 1):
        if ((num[cnt] != '0') and (num[cnt] != '1')):
            return 0
    return 1

def is_oct_valid (num):
    num = str(num)
    lim = len(num)
    for cnt in range(0, lim, 1):
        if ((num[cnt] == '9') or (num[cnt] == 'A') or (num[cnt] == 'B') or (num[cnt] == 'C') or (num[cnt] == 'D') or (num[cnt] == 'E') or (num[cnt] == 'F')):
            return 0
    return 1

def is_hex_valid (num):
    num = str(num)
    return 1

def array_to_array (arrGiven, arrGiver):
    lim = len(arrGiver)
    for cnt in range(0, lim, 1):
        arrGiven.append(arrGiver[cnt])

x = input("User, enter a number:\n")
dec_num = int(x)
bin_num = int(decimal_to_binary(x))
oct_num = int(decimal_to_octal(x))
hex_num = str(decimal_to_hexadecimal(x))
arr_dec = []
arr_bin = []
arr_oct = []
arr_hex = []
gen_arr = []

res_fr = '' # fresh results
res_conv = '' # converted results by random converter
sec_rndm_conv = '' # selected random conversion

digits_to_array(arr_dec, dec_num)
digits_to_array(arr_bin, bin_num)
digits_to_array(arr_oct, oct_num)
characters_to_array(arr_hex, hex_num)

array_to_array(gen_arr, arr_dec)
array_to_array(gen_arr, arr_bin)
array_to_array(gen_arr, arr_oct)
array_to_array(gen_arr, arr_hex)

res_fr = rndm_string_array(res_fr, gen_arr)
sec_rndm_conv = random_conversion_checker(res_fr)
print("The results are: " + str(sec_rndm_conv))
input("\nDONE!\n")
