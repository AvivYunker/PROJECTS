import random
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        arr = []
        print(str(lower), end=" --> (")
        digits_to_array(lower, arr)
        print_digits(arr)
        print(")", end=" --> (")
        use_array(arr)
        print(")")
        lower = int(lower + 1)
def digits_to_array (num, array):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        array.append(temp)
        num = int(num / 10)

def print_digits (arr):
    lim = len(arr)
    for cnt in range(lim-1, -1, -1):
        if (cnt == 0):
            print(str(arr[cnt]), end="")
        else:
            print(str(arr[cnt]), end=",")


def use_array (arr):
    lim = len(arr)
    for cnt in range(lim-1, -1, -1):
        if (cnt == 0):
            flag = int(0)
            random_num_digit(arr[cnt], flag)
        else:
            flag = int(1)
            random_num_digit(arr[cnt], flag)

def random_num_digit (num, flag):
    num = int(num)
    flag = int(flag)
    sums = int(0)
    level = int(1)
    while (num > 0):
        digit = int(random.randrange(0, 9))
        sums = int(sums + digit * level)
        level = int(level * 10)
        num = int(num - 1)

    if (flag == 0):
        print(str(sums), end="")
    else:
        print(str(sums), end=",")

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("DONE!\n")
