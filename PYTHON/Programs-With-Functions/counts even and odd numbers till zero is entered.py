# CREATED BY: Aviv Yunker
# NAME: "counts even and odd numbers till zero is entered"
# TAGS: even, odd, counter, zero, function, no-return, print, while, if-else
# EXPLANATION: this program will continue to receive numbers, until zero is entered.
# then - it will print back the count of entered even numbers, and the count
# of entered odd numbers

def even_odd_counter():
    x = input("User, enter a number: ")
    sumE = 0
    sumO = 0
    num = int(x)
    while num != 0:
        if num % 2 == 0:
            sumE = sumE + 1
        else:
            sumO = sumO + 1
        x = input("User, enter another number: ")
        num = int(x)
    print("\nNumber of even numbers: " + str(sumE) + "\nNumber of odd numbers: " + str(sumO) + "\n")

even_odd_counter()
input("\nDONE!\n")
