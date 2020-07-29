import random
def n_random_capital_letters (num):
    num = int(num)
    res = ""
    while (num > 0):
        rndm = random.randrange(65, 91)
        res += str(chr(rndm))
        num = int(num - 1)
    return res

file = open("test2.txt", "w")
x = input("User, how many letters?\n")
strr = n_random_capital_letters(x)
file.write(strr)
file.close()
input("\nDONE!\n")
