# CREATED BY: Aviv Yunker
# NAME: "custom triangle printer"
# TAGS: triangle, base, input, print, asterisks,
# EXPLANATION: this program will print a triangle (size of triangle base will be 'n' - the input)
# EXAMPLE:
#             *
#             **
# entered 4 - ***
#             ****
def triangle_printer(num):
    num = int(num);
    for cnt1 in range (0, num+1, 1):
        for cnt2 in range (0, cnt1, 1):
            print("*", end="");
        print("");
    print("");

x = input("User, enter base of triangle:\n");
x = int(x);

triangle_printer(x);
input("\nDONE!\n") # This holds the CLI.
