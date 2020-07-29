def factorial (num):
    num = int(num)
    res = int(1)
    while (num > 0):
        res *= num
        num -= 1
    return res

x = input("User, enter a number:\n")
x = int(x)

results = factorial(x)
print("The results are: " + str(results))
input("\nDONE!\n")