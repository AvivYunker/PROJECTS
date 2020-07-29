def digit_avg (num):
    num = int(num)
    sums = int(0)
    cnt = int(0)
    while (num > 0):
        temp = int(num % 10)
        sums = int(sums + temp)
        cnt = int(cnt + 1)
        num = int(num / 10)
    return (sums * 1.0 / cnt)


x = input("User, enter a number:\n")
x = int(x)

results = digit_avg(x)
print("The average of digits is: " + str(results))
input("\nDONE!\n")