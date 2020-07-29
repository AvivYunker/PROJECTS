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

x = input("User, enter a number:\n")
x = int(x)
results = decimal_to_hexadecimal(x)
print("The results are: " + str(results))
input("\nDONE!\n")