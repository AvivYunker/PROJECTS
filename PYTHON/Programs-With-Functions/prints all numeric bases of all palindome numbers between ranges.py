def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        results = is_palindrome(lower)
        if (results == 1):
            all_bases_printer(lower)
        lower = int(lower + 1)

def is_palindrome (num):
    num = int(num)
    arr = []
    digits_to_array(arr, num)
    lim = len(arr)
    cnt2 = int(lim-1)
    for cnt1 in range(0, lim, 1):
        if (arr[cnt1] != arr[cnt2]):
            return 0
        cnt2 = int(cnt2 - 1)
    return 1

def digits_to_array (arr, num):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def all_bases_printer (num):
    num = int(num)
    print("(" + str(num), end=") --> (BIN:")
    print(str(decimal_to_binary(num)), end=") --> (OCT:")
    print(str(decimal_to_octal(num)), end=") --> (HEX:")
    print(str(decimal_to_hexadecimal(num)) + ")")

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
    res = str('')
    while (num > 0):
        tempI = int(num / 16)
        tempF = float(num*1.0 / 16)
        tempF = float(tempF - tempI)
        tempF = int(tempF * 16)
        if (tempF == 10):
            arr.append('A')
        elif (tempF == 11):
            arr.append('B')
        elif (tempF == 12):
            arr.append('C')
        elif (tempF == 13):
            arr.append('D')
        elif (tempF == 14):
            arr.append('E')
        elif (tempF == 15):
            arr.append('F')
        else:
            tempF = int(tempF)
            arr.append(tempF)
        num = int(tempI)
    lim = len(arr)
    for cnt in range(lim-1, -1, -1):
        res += str(arr[cnt])
    return res

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n")
