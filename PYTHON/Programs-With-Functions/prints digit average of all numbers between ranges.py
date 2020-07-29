def between_ranges (lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        print(str(lower), end=" --> (");
        print(average_digit(lower), end="");
        print(")");
        lower = int(lower + 1);

def average_digit (num):
    num = int(num);
    d = int(digit_counter(num));
    sums = int(0);
    while (num > 0):
       temp = int(num % 10);
       sums = int(sums + temp);
       num = int(num / 10);
    results = float(sums*1.0 / d);
    return results


def digit_counter(x):
    x = int(x);
    counter = int(0);
    if (x == 0):
        counter = int(1);
    else:
        while (x > 0):
            counter = int(counter + 1);
            x = int(x / 10);
    return counter;

lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
input("\nDONE!\n")
