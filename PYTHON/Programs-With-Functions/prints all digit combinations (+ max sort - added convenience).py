def all_digit_combinations (num):
    num = int(num)
    lower = int(max_sort_StoL(num))
    upper = int(max_sort_LtoS(num))
    while (lower <= upper):
        results = is_digit_combination(lower, num)
        if (results == 1):
            print(str(lower))
        lower = int(lower + 1)

def is_digit_combination (temp, num):
    temp = int(temp)
    num = int(num)
    arrT = []
    arrN = []
    digits_to_array(temp, arrT)
    digits_to_array(num, arrN)
    res = cnt_digits_match (arrT, arrN)
    return res


def cnt_digits_match (arrTemp, arrDigits):
    limT = len(arrTemp)
    for cnt in range (0, 10, 1):
        counter1 = arrTemp.count(cnt)
        counter2 = arrDigits.count(cnt)
        if (counter1 != counter2):
            return 0
    return 1


def max_sort_StoL (num):
    num = int(num)
    res = int(0)
    arr = []
    arrNew = []
    digits_to_array(num, arr)
    max_sorter(arr, arrNew)
    res = array_to_number_StoL(arrNew, res)
    return res

def max_sort_LtoS (num):
    num = int(num)
    res = int(0)
    arr = []
    arrNew = []
    digits_to_array(num, arr)
    max_sorter(arr, arrNew)
    res = array_to_number_LtoS(arrNew, res)
    return res

def digits_to_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def max_sorter (arrO, arrN):
    lim = len(arrO)
    d = all_minus(arrO)
    while (d == 0):
        minimum = int(10)
        for cnt in range(0, lim, 1):
            if ((arrO[cnt] < minimum) and (arrO[cnt] != int(-1))):
                minimum = int(arrO[cnt])
                index = int(cnt)
        arrN.append(minimum)
        arrO[index] = int(-1)
        d = all_minus(arrO)

def array_to_number_StoL (arr, num):
    num = int(0)
    lim = len(arr)
    level = int(1)
    for cnt in range(lim-1, -1, -1):
        num = int(num + level * int(arr[cnt]))
        level = int(level * 10)
    return num

def array_to_number_LtoS (arr, num):
    num = int(0)
    lim = len(arr)
    level = int(1)
    for cnt in range(0, lim, 1):
        num = int(num + level * int(arr[cnt]))
        level = int(level * 10)
    return num

def all_minus (arr):
    lim = len(arr)
    for cnt in range(0, lim, 1):
        if (arr[cnt] != int(-1)):
            return 0
    return 1

x = input("User, enter a number:\n")
x = int(x)
print("\n")

all_digit_combinations(x)
input("\nDONE!\n")
