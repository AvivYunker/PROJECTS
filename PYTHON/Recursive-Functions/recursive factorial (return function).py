def recursive_factorial (num, res):
    num = int(num)
    res = int(res)
    while (num > 0):
        res = int(res * num)
        num = int(num - 1)
        recursive_factorial(num, res)
    return res

x = input("User, enter a number:\n")
x = int(x)
res = int(1)
results = recursive_factorial(x, res)
print("The results are: " + str(results))
input("\nDONE!\n")