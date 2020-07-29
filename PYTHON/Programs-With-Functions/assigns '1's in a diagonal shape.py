# CREATED BY: Aviv Yunker
# NAME: Assign '1' diagonally in a square of characters.
# TAGS: square, diagonal, print, zeros, ones, matrix, power, for-loop, range
# EXPLANATION: program will assign '1' characters in a diagonal position - to the
# characters - in a diagonal way.
# EXAMPLE:
# 000      100
# 000 ---> 010
# 000      001
def assign_array_size (arr, size):
    size = int(size)
    lim = int(pow(size, 2))
    for cnt in range(0, lim, 1):
        arr.append(int(0))

def assign_diagonal (arr):
    lim = len(arr)
    size = int(pow(lim, 0.5))
    for cnt in range (0, lim, size+1):
        arr[cnt] = int(1)

def print_array_contents (arr):
    lim = len(arr)
    size = int(pow(lim, 0.5))
    for cnt in range(0, lim, 1):
        if (cnt % size == 0):
            print("")
        print(str(arr[cnt]), end="")

x = input("User, size of matrix?\n")
size = int(x)
arr = []

assign_array_size(arr, size)
print_array_contents(arr)
print("\n\n")
assign_diagonal(arr)
print_array_contents(arr)
input("\nDONE!\n") # This holds the CLI.
