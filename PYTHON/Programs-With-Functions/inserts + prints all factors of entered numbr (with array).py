# CREATED BY: Aviv Yunker
# NAME: "inserts and prints all factors of entered number"
# TAGS: divisors, insert, print, list, factors, while, if, for-in
# EXPLANATION: This program will receive a number. And for that number - will
# insert all the divisors of that number to a list, and then will print all
# the divisors from that list.
# EXAMPLE:
# input: 1000 --> 1000,500,250,200,125,100,50,40,25,20,10,8,5,3,2,1
# will print: 1,2,3,5,8,10,20,25,40,50,100,125,200,250,500,1000

def all_factors_array (num, arr):
    num = int(num)
    b = int(num)
    while (b > 0):
        if (num % b == 0):
            arr.append(b)
        b = int(b - 1)

def array_contents_printer (arr):
    lim = len(arr)
    for cnt in range(0, lim, 1):
        print(str(arr[cnt]), end=",")
    print("")
    for cnt in range(lim-1, -1, -1):
        print(str(arr[cnt]), end=",")

x = input("User, enter a number:\n")
x = int(x)
arr = []

all_factors_array(x, arr)
array_contents_printer(arr)
input("\nDONE!\n") # This holds the CLI
