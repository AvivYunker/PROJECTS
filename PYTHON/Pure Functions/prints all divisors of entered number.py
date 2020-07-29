def all_divisors (arr, num):
    num = int(num)
    div = int(num)
    while (div > 0):
        if (num % div == 0):
            arr.append(div)
        div = int(div - 1)

def print_array_contents (arr):
    lim = len(arr)
    for cnt in range(0, lim, 1):
        if (cnt == (lim-1)):
            print(str(arr[cnt]), end=".")
        else:
            print(str(arr[cnt]), end=",")


x = input("User, enter a number:\n")
x = int(x)
arr = []

all_divisors(arr, x)
print_array_contents(arr)

input("\nDONE!\n")
