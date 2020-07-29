# CREATED BY: Aviv Yunker
# NAME: "Binary between ranges"
# EXPLANATION: this program prints all binary equivalents of
# the decimal numbers (that are between ranges).
# prints an annoying 'none' text after every results. //FIXED//
# TAGS: binary, decimal, ranges, while, convert, conversion, if,
def between_ranges(lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        decimal_to_binary(lower);
        lower = int(lower + 1);

def decimal_to_binary(num):
    num = int(num);
    cnt = int(0);
    arr = [];
    while (num > 0):
        tempI = int(num / 2);
        tempF = float(num / 2);
        tempF = float(tempF - tempI);
        tempF = int(tempF * 2);
        arr.insert(cnt, tempF);
        cnt = int(cnt + 1);
        num = int(tempI);
    max = len(arr);
    if (max == 0):
        print("0");
    else:
        for pos in range (max-1, -1, -1):
            print(arr[pos], end="");
        print("");

lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
input("\nDONE!\n") # This holds the CLI.
