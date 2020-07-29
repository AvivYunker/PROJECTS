import random
def between_ranges(lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        print(str(lower), end=" --> (")
        arr = []
        arrBin = []
        digits_to_array(lower, arr)
        print(")", end=" --> (")
        digit_array_user(arr, arrBin)
        print(")", end=" --> (")
        array_conversion(arrBin)
        print(")")
        lower = int(lower + 1)


def digits_to_array(num, arr):
    num = int(num)
    if (num == 0):
        arr.append(0)
    else:
        while (num > 0):
            temp = int(num % 10)
            arr.append(temp);
            num = int(num / 10)
    lim = len(arr)
    for cnt in range(lim-1, -1, -1):
        if (cnt == 0):
            print(str(arr[cnt]), end="")
        else:
            print(str(arr[cnt]), end=",")

def digit_array_user (arr, arrBin):
    lim = len(arr)
    for cnt in range(lim-1, -1, -1):
        if (cnt == 0):
            flag = int(0)
        else:
            flag = int(1)
        binary_boggler(arr[cnt], flag, arrBin)

def binary_boggler (num, flag, arrBin):
    num = int(num)
    flag = int(flag)
    sums = int(0)
    level = int(1)
    while (num > 0):
        temp = int(random.randrange(0, 2))
        sums = int(sums + temp*level)
        level = int(level * 10)
        num = int(num - 1)
    arrBin.append(sums)
    if (flag == 1):
        print(str(sums), end=",")
    else:
        print(str(sums), end="")

def array_conversion (arrBin):
    lim = len(arrBin)
    for cnt in range(0, lim, 1):
        res = binary_to_decimal(arrBin[cnt])
        if (cnt == (lim-1)):
            print(str(res), end="")
        else:
            print(str(res), end=",")

def binary_to_decimal (num):
    num = int(num);
    level = int(0);
    res = int(0);
    while (num > 0):
        temp = int(num % 10);
        res = int(res + temp * pow(2, level));
        num = int(num / 10);
        level = int(level + 1);
    return res;


def digit_counter (num):
    num = int(num)
    counter = int(0)
    if (num == 0):
        counter = int(1)
    else:
        while (num > 0):
            counter = int(counter + 1)
            num = int(num / 10)
    return counter

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("DONE!\n");
