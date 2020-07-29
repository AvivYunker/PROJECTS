def OR (num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    arr_bin_1 = []
    arr_bin_2 = []
    dec_res = int(0)
    decimal_toBinary_array(num1, arr_bin_1)
    decimal_toBinary_array(num2, arr_bin_2)
    binaryArray_size_equalizer(arr_bin_1, arr_bin_2)
    bin_res = OR_operator(arr_bin_1, arr_bin_2)
    dec_res = binary_to_decimal(bin_res)
    return dec_res

def decimal_toBinary_array (num, arr):
    num = int(num)
    binary = decimal_to_binary(num)
    insert_into_array(binary, arr)

def decimal_to_binary (num):
    num = int(num);
    sum = int(0);
    pusher = int(1);
    while (num > 0):
        temp = int(num % 2);
        sum = int(sum + temp * pusher);
        num = int(num / 2);
        pusher = int(pusher * 10);
    return sum;

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

def OR_operator (arr1, arr2):
    lim = len(arr1)
    res = int(0)
    level = int(1)
    for cnt in range(0, lim, 1):
        if (arr1[cnt] == 1 or arr2[cnt] == 1):
            val = int(1)
        else:
            val = int(0)
        res = int(res + int(val * level))
        level = int(level * 10)
    return res


def binary_to_decimal (num):
    num = int(num);
    sum = int(0);
    level = int(0);
    while (num > 0):
        temp = int(num % 10);
        temp = int(temp * pow(2,level));
        sum = int(sum + temp);
        level = int(level + 1);
        num = int(num / 10);
    return sum;

x = input("User, enter first number:\n")
y = input("User, enter second number:\n")

x = int(x)
y = int(y)

z = OR(x, y)
print("The results are: " + str(z))
input("\nDONE!\n")
