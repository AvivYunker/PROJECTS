# CREATED BY: Aviv Yunker
# NAME: "inserts and prints 'n' values from list"
# TAGS: list, insert, function, no-return, print, input
# EXPLANATION: This program will receive a number ('n'), and then request from
# the user to enter 'n' values. After that - those entered values will be printed.
# EXAMPLE:
# entered 4
# entered: 9,8,7,6
# will print: 9,8,7,6
def insert_into_array (arr, x):
    x = int(x)
    for cnt in range(0, x, 1):
        val = input("User, enter value no. " + str(cnt + 1) + "  ")
        arr.append(val)

def print_array_contents (arr):
    print("")
    lim = len(arr)
    for cnt in range(0, lim, 1):
        print(str(arr[cnt]), end=",")

x = input("User, array size?\n")
x = int(x)
arr = []

insert_into_array (arr, x)
print_array_contents (arr)
input("\nDONE!\n") # This holds the CLI.
