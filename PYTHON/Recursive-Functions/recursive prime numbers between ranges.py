# this will be 'recursive prime numbers between ranges'
def recursive_between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        results = is_prime(lower)
        if (results == 1):
            print(str(lower) + " is a prime")
        recursive_between_ranges(lower + 1, upper)

def is_prime(num):
    num = int(num)
    b = int(num - 1)
    while (b > 1):
        if (num % b == 0):
            return 0
        else:
            b = int(b - 1)
    return 1

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

recursive_between_ranges(lwr, upr)
input("DONE\n")
