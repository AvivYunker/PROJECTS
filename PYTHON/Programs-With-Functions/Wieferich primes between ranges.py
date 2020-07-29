def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        results = is_wieferich_prime(lower)
        if (results == 1):
            print(str(lower) + " is a Wieferich prime")
        lower = int(lower + 1)

def is_wieferich_prime (num):
    num = int(num)
    res1 = is_prime(num)
    if (res1 == 1):
        res2 = is_wieferich(num)
        if (res2 == 1):
            return 1
        else:
            return 0
    else:
        return 0

def is_prime (num):
    num = int(num);
    b = int(num - 1);
    while (b > 1):
        if (num % b == 0):
            return 0;
        b = int(b - 1);
    return 1;

def is_wieferich (num):
    num = int(num)
    num1 = int(pow(num, 2))
    num2 = int(pow(2, (num-1)) - 1)
    if (num1 == 0):
        return 0
    else:
        if (num2 % num1 == 0):
            return 1
        else:
            return 0

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n")
