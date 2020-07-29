def asterisk_scale_digits (num):
    num = int(num)
    arr = []
    digits_to_array(num, arr)
    asterisk_scale_printer(arr)


def digits_to_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def asterisk_scale_printer (arr):
    lim = len(arr)
    for cnt1 in range(lim-1, -1, -1):
        print(str(arr[cnt1]), end=" --> (")
        for cnt2 in range(0, 10, 1):
            if (arr[cnt1] == cnt2):
                print("*", end="")
            else:
                print("_", end="")
        print(")")

x = input("User, enter a number:\n")
x = int(x)
asterisk_scale_digits(x)
input("DONE!\n")
