def between_ranges (lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        print(str(lower), end=" --> (");
        prime_till_zero(lower);
        print(")");
        lower = int(lower + 1);

def prime_till_zero (num):
    num = int(num);
    up = int(num);
    lw = int(0);
    while (lw <= up):
        b = int(lw - 1);
        bad = int(0);
        while (b > 1):
            if (lw % b == 0):
                bad = int(bad + 1);
            b = int(b - 1);
        if (bad == 0):
            print(str(lw), end=",");
        lw = int(lw + 1);



lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
input("\nDONE!\n")
