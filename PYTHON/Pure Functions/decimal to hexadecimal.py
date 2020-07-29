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

x = input("User, enter a number:\n")
x = int(x)

results = decimal_to_hexadecimal(x)
print("The results are: " + str(results))
input("\nDONE!\n")
