def between_ranges (lower, upper, sums):
    lower = int(lower);
    upper = int(upper);
    sums = int(sums);
    while (lower <= upper):
        results = is_sum(lower, sums);
        if (results == 1):
            print(str(lower) + " has sum of: " + str(sums));
        lower = int(lower + 1);

def is_sum (num, sumss):
    num = int(num);
    sumss = int(sumss);
    tempSum = int(0);
    while (num > 0):
        temp = int(num % 10);
        tempSum = int(tempSum + temp);
        num = int(num / 10);
    if (tempSum == sumss):
        return 1;
    else:
        return 0;


lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");
sm = input("User, enter the requested sum:\n");

lwr = int(lwr);
upr = int(upr);
sm = int(sm);

between_ranges(lwr, upr, sm);
input("DONE!");