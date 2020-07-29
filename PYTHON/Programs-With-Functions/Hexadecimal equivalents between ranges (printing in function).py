# CREATED BY: Aviv Yunker
# TAGS: hexadecimal, decimal, ranges, while, no-return, convert, conversion
# EXPLANATION: this program will print all hexadecimal equivalents of the integers, that are between ranges.
# EXAMPLE:
# 1500 --> 5DC
# 1501 --> 5DD
def between_ranges (lower, upper):
    print("\n");
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        print(str(lower), end=" --> (")
        decimal_to_hexadecimal(lower);
        lower = int(lower + 1);
    print("\n");

def decimal_to_hexadecimal(num):
    num = int(num);
    arr = [];
    while (num > 0):
        tempI = int(num / 16);
        tempF = float(num / 16);
        tempF = float(tempF - tempI);
        tempF = int(tempF * 16);
        if (tempF == 10):
            tempF = 'A';
        elif(tempF == 11):
            tempF = 'B';
        elif(tempF == 12):
            tempF = 'C';
        elif(tempF == 13):
            tempF = 'D';
        elif(tempF == 14):
            tempF = 'E';
        elif(tempF == 15):
            tempF = 'F';
        arr.append(tempF);
        num = int(tempI);
    max = len(arr);
    if (max == 0):
        print("0");
    else:
        for cnt in range (max - 1, -1, -1):
            print(arr[cnt], end="");
        print(")");

lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr)
input("\nDONE!\n") # This holds the CLI.
