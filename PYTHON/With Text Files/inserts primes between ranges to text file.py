def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    res = ""
    while (lower <= upper):
        results = is_prime(lower)
        if (results == 1):
            res += str(lower) + "\n"
        lower = int(lower + 1)
    return res

def is_prime (num):
    num = int(num)
    b = int(num - 1)
    while (b > 1):
        if (num % b == 0):
            return 0
        b = int(b - 1)
    return 1

def insert_to_txt (strr):
    strr = str(strr)
    file = open("primes between ranges", "w")
    file.write(strr)
    file.close()

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

strr = between_ranges(lwr, upr)
insert_to_txt(strr)
input("\nDONE!\n")
