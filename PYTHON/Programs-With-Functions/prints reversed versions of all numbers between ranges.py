def between_ranges(lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        print(str(lower), end=" --> (")
        results = reverse_number(lower)
        print(str(results) + ")")
        lower = int(lower + 1)


def reverse_number (num):
    arr = []
    digits_to_array(num, arr)
    res = arr_to_number(arr)
    return res

def digits_to_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)
    lim = len(arr)

def arr_to_number (arr):
    lim = len(arr)
    number = int(0)
    level = int(1)
    for cnt in range(lim-1, -1, -1):
        number = int(number + arr[cnt]*level)
        level = int(level * 10)
    return number

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")
lwr = int(lwr)
upr = int(upr)
between_ranges(lwr, upr)
input("\nDONE!\n")