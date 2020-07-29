# CREATED BY: Aviv Yunker
# NAME: "counts and sums even and odd numbers
# TAGS: even, odd, count, sum, while, if-else, print, function, no-return
# EXPLANATION: this program will continue to ask for numeric input, as long as the
# input is different than zero. For each of these numbers - it will sum the even
# and odd numbers separately, and will count the even and odd numbers separately

def even_odd_counter_sum(num):
    num = int(num)
    cntE = int(0)
    cntO = int(0)
    sumE = int(0)
    sumO = int(0)
    while (num != 0):
        if (num % 2 == 0):
            cntE = int(cntE + 1)
            sumE = int(sumE + num)
        else:
            cntO = int(cntO + 1)
            sumO = int(sumO + num)
        num = input("User, enter another number")
        num = int(num)
    print("\n")
    print("Number of even numbers is: " + str(cntE))
    print("Sum of even numbers is: " + str(sumE))
    print("Number of odd numbers is: " + str(cntO))
    print("Sum of odd numbers is: " + str(sumO))
    print("\n")

x = input("User, enter a number:")
x = int(x)

even_odd_counter_sum(x)
input("\nDONE!\n") # This holds the CLI.
