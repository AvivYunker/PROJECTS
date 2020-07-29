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


x = input("User, enter a number:\n")
x = int(x)
multiple_digit_scale(x)
input("\nDONE!\n")
