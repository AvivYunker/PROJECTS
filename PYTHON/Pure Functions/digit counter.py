def digit_counter (num):
    num = int(num)
    counter = int(0)
    if (num == 0):
        counter = int(1)
    else:
        while (num > 0):
            num = int(num / 10)
            counter = int(counter + 1)
    return counter

x = input("User, enter a number:\n")
x = int(x)
cnt = int(digit_counter(x))
print("Total number of digits is: " + str(cnt))
input("\nDONE!\n")
