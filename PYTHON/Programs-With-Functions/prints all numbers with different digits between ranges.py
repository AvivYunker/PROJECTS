def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        results = are_different_digits(lower)
        if (results == 1):
            print(str(lower), end=",")
        lower = int(lower + 1)

def are_different_digits (num):
    num = int(num)
    arr = []
    digits_to_array(num, arr)
    lim = len(arr)
    for cnt1 in range(0, lim, 1):
        for cnt2 in range(0, lim, 1):
            if ((arr[cnt1] == arr[cnt2]) and (cnt1 != cnt2)):
                return 0
    return 1

def digits_to_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n")
