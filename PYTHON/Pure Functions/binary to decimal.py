def binary_to_decimal (num):
    num = int(num)
    level = int(0)
    res = int(0)
    while (num > 0):
        temp = int(num % 10)
        temp = int(temp * pow(2, level))
        res = int(res + temp)
        level = int(level + 1)
        num = int(num / 10)
    return res

x = input("User, enter BINARY number:\n")
x = int(x)

results = binary_to_decimal(x)
print("The results are: " + str(results))
input("\nDONE!\n")
