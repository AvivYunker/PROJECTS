# CREATED BY: Aviv Yunker
# NAME: "Hexadecimal Reverser for every decimal between ranges"
# TAGS: hexadecimal, reverse, decimal, if-else, function, return, ranges, while, if-else, for-in,
# EXPLANATION: This program will print all decimal between ranges - and for each decimal
# will print the hexadecimal equivalent, print the reversed hexadecimal, and print
# the reconverted decimal from the reversed hexadecimal.
# EXAMPLE:
# 15000 --> 3A98 --> 89A3 --> 35235
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        hexadecimal_reverser_presenter(lower)
        lower = int(lower + 1)

def hexadecimal_reverser_presenter (num):
    dec_orig = int(num)
    hex_orig = decimal_to_hexadecimal(dec_orig)
    hex_rev = hexadecimal_reverser(hex_orig)
    dec_trs = hexadecimal_to_decimal(hex_rev)
    print("(DEC_ORIG: " + str(dec_orig), end=") / ")
    print("(HEX_ORIG: " + str(hex_orig), end=") / ")
    print("(HEX_REV: " + str(hex_rev), end=") / ")
    print("(DEC_TRS: " + str(dec_trs), end=")")
    print("")

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


def hexadecimal_reverser (num):
    num = str(num)
    res = ""
    arrOld = []
    arrNew = []
    characters_to_array(arrOld, num)
    hex_reverse(arrNew, arrOld)
    res = characters_to_string(arrNew)
    return res

def characters_to_array (arr, num):
    num = str(num)
    lim = len(num)
    for cnt in range(0, lim, 1):
        arr.append(str(num[cnt]))

def hex_reverse (arrN, arrO):
    lim = len(arrO)
    for cnt in range(lim-1, -1, -1):
        arrN.append(str(arrO[cnt]))

def characters_to_string (arr):
    lim = len(arr)
    res = ""
    for cnt in range(0, lim, 1):
        res += str(arr[cnt])
    return res

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n") # This holds the CLI.
