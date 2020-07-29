def number_reverser (num):
    num = int(num)
    res = int(0)
    dig = int(digit_counter(num))
    level = int(dig - 1)
    while (num > 0):
        temp = int(num % 10)
        res += temp * pow(10, level)
        level -= 1
        num = int(num / 10)
    return res

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
results = number_reverser(x)
print("The results are: " + str(results))
input("\nDONE!\n")
