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

digit_asterisk_scale(x)
