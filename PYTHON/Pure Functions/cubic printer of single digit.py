def cubic_printer (num):
    num = int(num)
    print("")
    if (num >= 0 and num <= 9):
        for cnt in range(1, 10, 1):
            if ((cnt-1) % 3 == 0):
                print("")
            if (cnt == num):
                print(str(num), end=" ")
            else:
                print(str("X"), end=" ")

x = input("User, enter a digit:\n")
x = int(x)
cubic_printer(x)
input("\nDONE!\n")
