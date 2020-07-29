def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        results = is_armstrong(lower)
        if (results == 1):
            print(str(lower), end=" --> (BIN:")
            print(decimal_to_binary(lower), end=") --> (OCT:")
            print(decimal_to_octal(lower), end=") --> (HEX:")
            print(decimal_to_hexadecimal(lower) + ")")
        lower = int(lower + 1)

def is_armstrong (num):
    num = int(num)
    orig = int(num)
    dig = digit_counter(num)
    sums = int(0)
    while (num > 0):
        temp = int(num % 10)
        temp = int(pow(temp, dig))
        sums = int(sums + temp)
        num = int(num / 10)
    if (sums == orig):
        return 1
    else:
        return 0

def digit_counter (num):
    num = int(num)
    counter = int(0)
    if (num == 0):
        counter = int(1)
    else:
        while (num > 0):
            num = int(num / 10)
            counter = int(counter + 1)
    return counter

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
