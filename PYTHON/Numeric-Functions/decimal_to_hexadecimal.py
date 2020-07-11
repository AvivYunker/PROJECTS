def decimal_to_hexadecimal (num):
    num = int(num)
    strr = str("")
    res = str("")
    while (num > 0):
        tempI = int(num / 16)
        tempF = float(num / 16.0)
        tempF = float(tempF - tempI)
        tempF = int(tempF * 16)
        if (tempF >= 0 and tempF <= 9):
            strr += str(tempF)
        else:
            tempF = int(tempF + 55)
            strr += chr(tempF)
        #print(tempF)
        num = int(tempI)
    lim = len(strr)
    for cnt in range(lim-1, -1, -1):
        res += str(strr[cnt])
    return res

x = int(input("User, enter a DECIMAL number: "))
results = decimal_to_hexadecimal(x)
print(str(x) + " --> " + str(results)) 
