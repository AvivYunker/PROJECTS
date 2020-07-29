# CREATED BY: Aviv Yunker
# NAME: cubic-view printer of single digit
# TAGS: cubic, view, printer, no-return, if-else, for-in, asterisks,
# EXPLANATION: this will print the cubic-view of a single digit only.
# EXAMPLE:
#      X X X      X X X
#  4 - 4 X X  8 - X X X
#      X X X      X 8 X
def cubic_view_printer (dig):
    dig = int(dig)
    print("\n")
    for cnt in range(1, 10, 1):
        if (cnt != dig):
            print("X ", end="")
        else:
            print(str(cnt) + " ", end="")
        if (cnt % 3 == 0):
            print("")

x = input("User, enter a number:\n")
x = int(x)

if (x >= 0 and x <= 9):
    cubic_view_printer(x)
else:
    print("Ivalid number...")
input("\nDONE!\n") # This holds the CLI.
