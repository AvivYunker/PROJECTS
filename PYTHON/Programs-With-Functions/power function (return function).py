def power_function (base, power):
    base = int(base)
    power = int(power)
    res = int(1)
    while (power > 0):
        res = int(res * base)
        power = int(power - 1)
    return res


x = input("User, enter the base:\n")
y = input("User, enter the power:\n")

x = int(x)
y = int(y)

results = power_function(x, y)
print("\nThe results are: " + str(results))
input("\nDONE!\n")
