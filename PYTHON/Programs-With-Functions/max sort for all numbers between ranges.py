def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        print(str(lower), end=" --> (")
        results = digit_sorter(lower)
        print(str(results) + ")")
        lower = int(lower + 1)

def digit_sorter(num):
    num = int(num)
    arr = []
    number_to_array(num, arr)
    sorter(arr)
    results = array_to_number(arr)
    return results

def number_to_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def sorter (arr):
    lim = len(arr)
    small = int(10)
    place = int(0)
    for cnt1 in range(0, lim, 1):
        for cnt2 in range(cnt1, lim, 1):
           if (arr[cnt2] < small):
              small = int(arr[cnt2])
              place = int(cnt2)
        temp = int(arr[cnt1])
        arr[cnt1] = int(small)
        arr[place] = int(temp)
        small = int(10)

def array_to_number (arr):
    lim = len(arr)
    res = int(0)
    level = int(1)
    for cnt in range(lim-1, -1, -1):
        res = int(res + level*arr[cnt])
        level = int(level * 10)
    return res

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n")
