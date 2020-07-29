# CREATED BY: Aviv Yunker
# NAME: "cubic view of multiple digits of a single number"
# TAGS: cubic, view, printer, no-return, if-else, for-in, asterisks, while, length, list,
# EXPLANATION: This will print the cubic view of a single give number. A cubic view
# is where we see what digits had appeared at-least once in the number. If the digit
# does exist within the number - it will show the digit. Otherwise - will print
# an 'X'.
# EXAMPLE:
#       1 2 X        X X X
# 412 - 4 X X  998 - X X X
#       X X X        X 8 9
def digits_to_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def cubic_viewer_array (arr):
    lim = len(arr)
    print("\n")
    for cnt in range(1, 10, 1):
        x = arr.count(cnt)
        if (x > 0):
            print(str(cnt) + " ", end="")
        else:
            print("X ", end="")
        if (cnt % 3 == 0):
            print("")
    print("\n")


x = input("User, enter a number:\n")
x = int(x)
arr = []

digits_to_array(x, arr)
cubic_viewer_array(arr)
input("\nDONE!\n") # This holds the CLI.
