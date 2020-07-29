def avg_char (strr):
    strr = str(strr)
    lim = len(strr)
    summ = int(0)
    for cnt in range(0, lim, 1):
        temp = ord(strr[cnt])
        summ = int(summ + temp)
    summ = int(summ*1.0 / lim)
    res = chr(summ)
    return res

x = input("User, enter a string:\n")
x = str(x)

y = avg_char(x)
print("The results are: " + str(y))
input("\nDONE!\n")
