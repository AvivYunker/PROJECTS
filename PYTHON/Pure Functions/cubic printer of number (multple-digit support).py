def cubic_printer (num):
    num = int(num)
    arr = []
    digits_to_array(arr, num)
    for cnt in range(1, 10, 1):
        if ((cnt-1) % 3 == 0):
            print("")
        if (arr.count(cnt) > 0):
            print(str(cnt), end=" ")
        else:
            print(str("X"), end=" ")
    print("")

def digits_to_array (arr, num):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

x = input("User, enter a number:\n")
x = int(x)
cubic_printer(x)
input("\nDONE!\n")
