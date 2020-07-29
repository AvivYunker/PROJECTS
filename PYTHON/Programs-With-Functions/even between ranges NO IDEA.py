
def between_ranges(lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        results = is_armstrong(lower);
        if (results == 1):
            print(str(lower) + " is an Armstrong");
        lower = int(lower + 1);

def is_armstrong(num):
    num = int(num);
    orig = int(num);
    d = digit_counter(num);
    sum = int(0);
    while (num > 0):
        temp = int(num % 10);
        temp = pow(temp, d);
        sum = int(sum + temp);
        num = int(num / 10);
    if (sum == orig):
        return 1;
    else:
        return 0;

def digit_counter (x):
    x = int(x);
    counter = int(0);
    if (x == 0):
        counter = 1;
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
input("DONE!\n");