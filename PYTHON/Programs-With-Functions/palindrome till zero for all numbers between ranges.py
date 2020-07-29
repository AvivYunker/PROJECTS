def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        arr = []
        print(str(lower), end=" --> (")
        palindrome_till_zero(lower)
        print(")")
        lower = int(lower + 1)


def palindrome_till_zero (num):
    num = int(num)
    while (num > 0):
        arr = []
        digits_to_array(num, arr)
        res = is_palindome(arr)
        if (res == 1):
            print(str(num) , end=",")
        num = int(num - 1)

def digits_to_array(num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)


def is_palindome (arr):
    lim = len(arr)
    j = int(lim -1)
    for cnt in range(0, lim, 1):
        if (arr[cnt] != arr[j]):
            return 0
        else:
            j = int(j - 1)
    return 1



lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n")
