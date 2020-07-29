import random
def n_hexadecimal_digits (num):
    num = int(num)
    while (num > 0):
        dig = random.randrange(0, 16)
        if (dig == 10):
            dig = 'A'
        elif (dig == 11):
            dig = 'B'
        elif (dig == 12):
            dig = 'C'
        elif (dig == 13):
            dig = 'D'
        elif (dig == 14):
            dig = 'E'
        elif (dig == 15):
            dig = 'F'
        else:
            dig = int(dig)
        print(str(dig), end="")
        num = int(num - 1)


x = input("User, how many hexadecimal digits?\n")
x = int(x)
n_hexadecimal_digits(x)
input("\nDONE!\n")
