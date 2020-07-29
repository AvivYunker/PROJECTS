def between_ranges (lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        all_divisors(lower);
        lower = int(lower + 1);

def all_divisors(num):
    num = int(num);

    print(str(num) + " ---> (", end="");
    d = int(num - 1);
    while (d > 0):
        if (d == 1):
            print(" " + str(d) + ")");
        else:
            if (num % d == 0):
                print(" "  + str(d) + ",", end="");
        d = int(d - 1);


lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
input("\nDONE!\n");