# CREATED BY: Aviv Yunker
# NAME: "inserts and prints all primary components of number"
# TAGS: primary-component, list, if-else, while, for-in, print, function, no-return
# EXPLANATION: For the entered number - it will insert all the primary components
# into a list - and then will print them from that list.
# EXAMPLE:
# 100 --> 2,2,5,5 (because 2*2*5*5 = 100)
# 15000 --> 2,2,2,3,5,5,5,5 (because 2*2*2*3*5*5*5*5 = 15000)
def all_prime_components (num, arr):
    num = int(num)
    b = int(2)
    while (num > 1):
        while (num % b == 0):
            arr.append(b)
            num = int(num / b)
        b = int(b + 1)


def print_array_contents (arr):
    lim = len(arr)
    for cnt in range(0, lim, 1):
        if (cnt == lim-1):
            print(str(arr[cnt]), end=".")
        else:
            print(str(arr[cnt]), end=",")



x = input("User, enter a number:\n")
x = int(x)
arr = []
all_prime_components(x, arr)
print_array_contents(arr)
input("\nDONE!\n") # This holds the CLI.
