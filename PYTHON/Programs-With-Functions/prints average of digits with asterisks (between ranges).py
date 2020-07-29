def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        print(str(lower), end=" --> (")
        lim = average_number(lower)
        for cnt in range(0, lim, 1):
            print("*", end="")
        print(")")
        lower = int(lower + 1)

def average_number(num):
    d = digit_counter(num)
    num = int(num)
    sums = int(0)
    while (num > 0):
        temp = int(num % 10)
        sums = int(sums + temp)
        num = int(num / 10)
    avg = int(sums / d)
    return avg

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

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("DONE!\n")
