def celsius_to_fahrenheit (num):
    num = int(num)
    res = (float)(1.8 * num + 32)
    return res

x = input("User, enter temperature (C)\n")
x = float(x)
y = celsius_to_fahrenheit(x)
print("The temperature in fahrenheit is: " + str(y))
input("\nDONE!\n")
