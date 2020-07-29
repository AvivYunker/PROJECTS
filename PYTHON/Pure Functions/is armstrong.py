def is_armstrong (num):
    num = int(num)
    orig = int(num)
    dig = digit_counter(num)
    sums = int(0)
    while (num > 0):
        temp = int(num % 10)
        temp = int(pow(temp, dig))
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

x = input("User, enter a number\n")
x = int(x)

results = is_armstrong(x)
if (results == 1):
    print("Is an Armstrong")
else:
    print("Is NOT an Armstrong")
input("\nDONE!\n")
