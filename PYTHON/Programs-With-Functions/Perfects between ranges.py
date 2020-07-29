def between_ranges(lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        results = is_perfect(lower);
        if (results == 1):
            print(str(lower) + " is perfect");
        lower = int(lower + 1);

def is_perfect (num):
    num = int(num);
    sum = int(0);
    b = int(num - 1);
    while (b > 0):
        if (num % b == 0):
            sum = int(sum + b);
        b = int(b - 1);
    if (num == sum):
        return 1;
    else:
        return 0;

lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
input("DONE!\n");