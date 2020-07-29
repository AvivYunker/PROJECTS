# CREATED BY: Aviv Yunker
# NAME: "AND logical operation between 2 integers"
# TAGS: AND, logical, operation, integers, return, list, binary, conversion, modulus, equalizer
# EXPLANATION: this program will perform the AND logical operation between 2 inputted integers.
# and will print the results.
# EXAMPLE:
# 5 AND 7
# 0101
# 0111
# 0101 = 5. Final results --> 5.
def AND(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    arr_bin_1 = []
    arr_bin_2 = []
    dec_res = int(0)
    decimal_toBinary_array(num1, arr_bin_1)
    decimal_toBinary_array(num2, arr_bin_2)
    binaryArray_size_equalizer(arr_bin_1, arr_bin_2)
    bin_res = AND_operator(arr_bin_1, arr_bin_2)
    dec_res = binary_to_decimal(bin_res)
    return dec_res

def decimal_toBinary_array (num, arr):
    num = int(num)
    binary = decimal_to_binary(num)
    insert_into_array(binary, arr)

def decimal_to_binary (num):
    num = int(num);
    sums = int(0);
    pusher = int(1);
    while (num > 0):
        temp = int(num % 2);
        sums = int(sums + temp * pusher);
        num = int(num / 2);
        pusher = int(pusher * 10);
    return sums;

def insert_into_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def binaryArray_size_equalizer (arr1, arr2):
    lim1 = len(arr1)
    lim2 = len(arr2)
    while (lim1 < lim2):
        arr1.append(0)
        lim1 = len(arr1)
    while (lim1 > lim2):
        arr2.append(0)
        lim2 = len(arr2)

def AND_operator (arr1, arr2):
    lim = len(arr1)
    res = int(0)
    level = int(1)
    for cnt in range(0, lim, 1):
        res = int(res + int(arr1[cnt] * arr2[cnt]) * level) # THIS IS THE PROBLEM!!!
        level = int(level * 10)
    return res


def binary_to_decimal (num):
    num = int(num);
    sums = int(0);
    level = int(0);
    while (num > 0):
        temp = int(num % 10);
        temp = int(temp * pow(2,level));
        sums = int(sums + temp);
        level = int(level + 1);
        num = int(num / 10);
    return sums;


x = input("User, enter first number:\n")
y = input("User, enter second number:\n")
z = AND(x, y)

print("The results are: " + str(z))
input("\nDONE!\n") # this holds the CLI.
