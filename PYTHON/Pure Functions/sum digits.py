def sum_digits (num):
    num = int(num)
    sums = int(0)
    while (num > 0):
        temp = int(num % 10)
        sums = int(sums + temp)
        num = int(num / 10)
    return sums

x = input("User, enter a number:\n")
x = int(x)

results = sum_digits(x)
print("The sum of the digits is: " + str(results))
input("\nDONE!\n")
