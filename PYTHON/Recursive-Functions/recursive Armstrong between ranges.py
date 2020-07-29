def recursive_between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        results = is_armstrong(lower)
        if (results == 1):
            print(str(lower) + " is an Armstrong")
        recursive_between_ranges (lower + 1, upper)

def is_armstrong (num):
    num = int(num)
    orig = int(num)
    d = digit_counter(num)
    sums = int(0)
    while (num > 0):
        temp = int(num % 10)
        temp = pow(temp, d)
        sums = int(sums + temp)
        num = int(num / 10)
    if (sums == orig):
        return 1
    else:
        return 0

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

recursive_between_ranges(lwr, upr)
print("DONE!\n")
