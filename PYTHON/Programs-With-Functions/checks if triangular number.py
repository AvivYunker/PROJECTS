# CREATED BY: Aviv Yunker
# NAME: "checks if triangular number"
# TAGS: triangular, if-else, while, return, function, input, output
# EXPLANATION: a triangular number counts objects, that continuously increases by 1.
# EXAMPLE:
# 10 --> 1+2+3+4 = 10 --> 10 is triangular.
# 8 --> 1+2+3 = 6 / 1+2+3+4 = 10 --> 8 is NOT triangular.

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

x = input("User, enter a number:\n")
x = int(x)

results = is_triangular(x)
if (results == 1):
    print(str(x) + " IS a triangular number")
else:
    print(str(x) + " is NOT a triangular number")
input("\nDONE!\n") # This holds the CLI.
