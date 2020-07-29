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


x = input("User, enter a HEXADECIMAL number:\n")
x = str(x)

results = hexadecimal_to_decimal(x)
print("The results are: " + str(results))
input("\nDONE!\n")
