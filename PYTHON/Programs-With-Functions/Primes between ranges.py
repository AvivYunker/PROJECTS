def between_ranges (lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        results = is_prime(lower);
        if (results == 1):
            print(str(lower) + " is prime");
        lower = int(lower + 1);
    print("DONE!\n");

def is_prime (num):
    num = int(num);
    b = int(num - 1);
    while (b > 1):
        if (num % b == 0):
            return 0;
        b = int(b - 1);
    return 1;

lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
input("DONE!\n");