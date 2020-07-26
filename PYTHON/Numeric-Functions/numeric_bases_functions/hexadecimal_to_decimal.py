def hexadecimal_to_decimal (num):
    num = str(num)
    lim = len(num)
    res = int(0)
    level = int(0)
    for cnt in range(lim-1, -1, -1):
        if ((ord(num[cnt]) >= 65) and (ord(num[cnt]) <= 90)):
            res += (ord(num[cnt])-55) * pow(16,level)
        elif ((ord(num[cnt]) >= 97) and (ord(num[cnt]) <= 122)):
            res += (ord(num[cnt])-87) * pow(16,level)
        else:
            res += (ord(num[cnt])-48) * pow(16,level)
        level = int(level + 1)
    return res



x = input("User, enter a HEXADECIMAL number: ")
results = hexadecimal_to_decimal(x)
print(str(x) + " --> " + str(results))
