def between_ranges (lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        print(str(lower), end=" --> (");
        max_min_digits(lower);
        print(")");
        lower = int(lower + 1);

def max_min_digits (num):
    maxi = int(0);
    mini = int(9);
    while (num > 0):
        temp = int(num % 10);
        if (temp >= maxi):
            maxi = int(temp);
        if (temp <= mini):
            mini = int(temp);
        num = int(num / 10);
    print("max digit:" + str(maxi) + " / min digit:" + str(mini), end="");

lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
input("DONE!\n");
