def all_digit_combination (num):
    num = int(num)
    arr = []
    d_count = digit_counter(num)
    digits_to_array(num, arr)
    lower = int(pow(10, d_count-1))
    upper = int(pow(10, d_count) - 1)
    while (lower <= upper):
        arrTemp = []
        digits_to_array(lower, arrTemp)
        results = cnt_digits_match(arrTemp, arr)
        if (results == 1):
            print(str(lower))
        lower = int(lower + 1)

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

def digits_to_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def cnt_digits_match (arrTemp, arrDigits):
    limT = len(arrTemp)
    for cnt in range (0, 10, 1):
        counter1 = arrTemp.count(cnt)
        counter2 = arrDigits.count(cnt)
        if (counter1 != counter2):
            return 0
    return 1

def array_printer (arr):
    lim = len(arr)
    for cnt in range(0, lim, 1):
        print(str(arr[cnt]), end=",")



x = input("User, enter a number:\n")
x = int(x)
print("\n")
all_digit_combination(x)
input("\nDONE!\n")
