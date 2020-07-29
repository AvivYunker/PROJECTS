def recursive_factorial (num, res):
    num = int(num)
    res = int(res)
    if (num > 0):
        res = int(res * num)
        recursive_factorial(num-1, res)
    else:
        print("The results are: " + str(res))

x = input("User, enter a number:\n")
x = int(x)
res = int(1)
recursive_factorial(x, res)
input("\nDONE!\n")
