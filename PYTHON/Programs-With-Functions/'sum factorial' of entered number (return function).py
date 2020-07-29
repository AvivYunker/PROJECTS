def sum_factorial (num):
    num = int(num)
    res = int(0)
    while (num > 0):
        res = int(res + num)
        num = int(num - 1)
    return res

x = input("User, enter a number:\n")
x = int(x)

results = sum_factorial(x)
print("the 'sum factorial' of " + str(x) + " is: " + str(results))
