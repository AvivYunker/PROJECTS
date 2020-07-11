def is_prime (num):
    num = int(num)
    b = int(num - 1)
    while (b > 1):
        if (num % b == 0):
            return 0
        b = int(b - 1)
    return 1

x = int(input("User, enter a number: "))
results = is_prime(x)
if (results == int(0)):
    print(str(x) + " is NOT a prime")
else:
    print(str(x) + " IS a prime")
