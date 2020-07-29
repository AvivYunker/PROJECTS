def is_prime (num):
    num = int(num)
    b = int(num - 1)
    while (b > 1):
        if (num % b == 0):
            return 0
        b = int(b - 1)
    return 1

x = input("User, enter a number:\n")
x = int(x)

results = is_prime(x)
if (results == 1):
    print("Is prime")
else:
    print("Is NOT prime")
input("\nDONE!\n")
