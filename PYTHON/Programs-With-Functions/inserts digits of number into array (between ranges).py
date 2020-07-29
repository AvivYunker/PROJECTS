# CREATED BY: Aviv Yunker
# NAME: "digits of entered number into array"
# TAGS: boggler, list, len, insert, for-in, while, function, no-return, print
# EXPLANATION: This program receives a single number, then will insert the digits
# of that number - and will print the contents of the list (the digits).
# EXAMPLE:
# 9912 --> 9 9 1 2
# 1234 --> 1 2 3 4
def number_boggler (num):
    num = int(num)
    arr = []
    insert_into_array(num, arr)

def insert_into_array(num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)
    lim = len(arr)
    for cnt in range (lim-1, -1, -1):
        print(str(arr[cnt]), end=" ")



x = input("User, enter a number:\n")
x = int(x)

number_boggler(x)
input("\nDONE!\n") # This holds the CLI.
