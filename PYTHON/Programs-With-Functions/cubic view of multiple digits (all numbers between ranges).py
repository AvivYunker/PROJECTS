# CREATED BY: Aviv Yunker
# NAME: "cubic view of all digits of entered number.#
# TAGS: cubic, view, printer, no-return, if-else, for-in, asterisks, while, length, list, ranges
# EXPLANATION: This will print a cubic view for all the digits of the entered number, for each number
# between ranges.
# EXAMPLE:
#       1 2 X        X X X
# 412 - 4 X X  998 - X X X
#       X X X        X 8 9
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        arr = []
        print("-" + str(lower) + "-", end="")
        digits_to_array(lower, arr)
        cubic_viewer_array(arr)
        lower = int(lower + 1)

def digits_to_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def cubic_viewer_array (arr):
    lim = len(arr)
    print("")
    for cnt in range(1, 10, 1):
        x = arr.count(cnt)
        if (x > 0):
            print(str(cnt) + " ", end="")
        else:
            print("X ", end="")
        if (cnt % 3 == 0):
            print("")
    print("\n")

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n") # This holds the CLI.
