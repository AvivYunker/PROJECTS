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

x = input("User, enter an OCTAL number:\n")
x = int(x)

results = octal_to_decimal(x)
print("The results are: " + str(results))
input("\nDONE!\n")
