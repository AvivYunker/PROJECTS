def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        print(str(lower), end=" --> ")
        multiple_digit_scale(lower)
        lower = int(lower + 1)


def multiple_digit_scale (num):
    num = int(num)
    arr = []
    digits_to_array(arr, num)
    lim = len(arr)
    print("(", end="")
    for cnt in range(0, 10, 1):
        sec = arr.count(cnt)
        if (sec > 0):
            print("*", end="")
        else:
            print("_", end="")
    print(")")

def digits_to_array (arr, num):
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
