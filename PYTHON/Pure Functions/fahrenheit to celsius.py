def fahrenheit_to_celsius (num):
    num = int(num)
    res = (num - 32) / (1.8)
    return res

x = input("User, enter temperature (F)\n")
x = float(x)
y = fahrenheit_to_celsius(x)
print("The temperature in celsius is: " + str(y))
input("\nDONE!\n")
