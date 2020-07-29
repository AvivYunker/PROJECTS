import random
def n_hexadecimal_digits (num):
    num = int(num)
    while (num > 0):
        rndm = random.randrange(0, 16)
        if (rndm == 10):
            rndm = 'A'
        elif (rndm == 11):
            rndm = 'B'
        elif (rndm == 12):
            rndm = 'C'
        elif (rndm == 13):
            rndm = 'D'
        elif (rndm == 14):
            rndm = 'E'
        elif (rndm == 15):
            rndm = 'F'
        else:
            rndm = int(rndm)
        print(str(rndm), end=",")
        num = int(num - 1)

x = input("User, how many random hexadecimal digits?\n")
x = int(x)
n_hexadecimal_digits(x)
input("\nDONE!\n")
