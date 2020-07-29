def digits_to_array (arr, num):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def scan_array (arr):
    lim = len(arr)
    for cnt in range(lim-1, -1, -1):
        digit_asterisk_scale(arr[cnt])

def digit_asterisk_scale (num):
    num = int(num)
    print("(", end="")
    for cnt in range(0, 10, 1):
        if (cnt == num):
            print("*", end="")
        else:
            print("_", end="")
    print(")")


x = input("User, enter a number:\n")
x = int(x)
arr = []
digits_to_array(arr, x)
scan_array(arr)
input("\nDONE!\n")