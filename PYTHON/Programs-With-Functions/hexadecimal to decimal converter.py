# CREATED BY: Aviv Yunker
# NAME: "hexadecimal to decimal converter"
# TAGS: hexadecimal, decimal, coversion, for-in, if-elif, function, return
# EXPLANATION: This program will receive a hexadecimal number - and print the
# converted decimal equivalent of the hexadecimal number.
# EXAMPLE:
# ABCD --> 43981
# A1B1C1D1 --> 2712781265
def hexadecimal_to_decimal (num):
    num = str(num);
    lim = len(num);
    level = int(0);
    res = int(0);
    arr = [];
    for cnt1 in range (0, lim, 1):
        arr.append(num[cnt1]);

    for cnt2 in range (lim - 1, -1, -1):
        if (arr[cnt2] == 'A' or arr[cnt2] == 'a'):
            temp = int(10);
        elif(arr[cnt2] == 'B' or arr[cnt2] == 'b'):
            temp = int(11);
        elif(arr[cnt2] == 'C' or arr[cnt2] == 'c'):
            temp = int(12);
        elif(arr[cnt2] == 'D' or arr[cnt2] == 'd'):
            temp = int(13);
        elif(arr[cnt2] == 'E' or arr[cnt2] == 'e'):
            temp = int(14);
        elif(arr[cnt2] == 'F' or arr[cnt2] == 'f'):
            temp = int(15);
        elif (int(arr[cnt2]) >= 0 and int(arr[cnt2]) <= 9):
            temp = int(arr[cnt2]);
        else:
            print("ERROR! not a hexadecimal number!");
            return 0;
        res = int(res + temp * pow(16, level));
        level = int(level + 1);

    return res;


x = input("User, enter a hexadecimal number:\n");
x = str(x);
results = hexadecimal_to_decimal(x);
print("The decimal equivalent is: " + str(results));
input("\nDONE!\n"); # This holds the CLI.
