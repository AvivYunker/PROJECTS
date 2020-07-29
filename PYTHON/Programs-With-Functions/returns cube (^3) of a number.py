def cube (num):
    res = num*num*num
    return res

x = input("User, enter a number:\n")
x = int(x)
results = int(cube(x))
print("the cube of " + str(x) + " is: " + str(results))
