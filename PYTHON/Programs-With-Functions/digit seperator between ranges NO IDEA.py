import random
def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    arr = []
    while (lower <= upper):
        print(str(lower), end=" --> (")
        digits_to_array(lower, arr)
        print(")", end=" --> (")
        array_digit_user(arr)
        print(")")
        lower = int(lower + 1)

def digits_to_array (num, arr):
    num = int(num)
    if (num == 0):
        arr.append(0)
    else:
        while (num > 0):
            temp = int(num % 10)
            arr.append(temp)
            num = int(num / 10)
        lim = len(arr)
        for cnt in range (lim-1, -1, -1):
            if (cnt == 0):
                print(str(arr[cnt]), end="")
            else:
                print(str(arr[cnt]), end=",")
        return arr

def array_digit_user(arr):
    lim = len(arr)
    for cnt in range(lim-1, -1, -1):
        binary_digit_randomizer(arr[cnt])

def binary_digit_randomizer (num):
    num = int(num)
    sum = int(0)
    d = int(digit_counter(num))
    avdD = int(0)
    level = int(1)
    while (avdD < d):
        temp = int(random.randrange(0,2))
        temp = int(temp*level)
        sum = int(temp);
        avdD = int(avdD + 1)
        level = int(level * 10)
    print(sum, end=" --> ")
    sums = int(binary_to_decimal(sum))
    print(sum, end=",")

def digit_counter(num):
    num == int(num)
    counter = int(0)
    if (num == 0):
        counter = int(1)
    else:
        while (num > 0):
            counter = int(counter + 1)
            num = int(num / 10)
    return counter

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


lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n")
