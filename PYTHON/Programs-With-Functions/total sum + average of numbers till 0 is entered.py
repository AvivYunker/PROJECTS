def sum_average_till_zero ():
    num = int(1)
    sums = int(0)
    count = int(0)
    while (num != 0):
        num = input("user, enter a number:\n")
        num = int(num)
        sums = int(sums + num)
        count = int(count + 1)
    avg = float(sums / count)
    print("The total sum is: " + str(sums) + " and the average is: " + str(avg))


sum_average_till_zero()
