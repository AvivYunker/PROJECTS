def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        results = is_triangular(lower)
        if (results == 1):
            print(str(lower) + " is a triangular number")
        lower = int(lower + 1)

def is_triangular (num):
    num = int(num)
    scannedSum = 0
    adder = int(1)
    while (scannedSum <= num):
        scannedSum = int(scannedSum + adder)
        if (scannedSum == num):
            return 1
        adder = int(adder + 1)
    return 0


lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n")
