# this program prints all numbers where the sum of odd digits equal to the sum of even digits
# TAGS: sum, digits, even, odd, equal, return, ranges,
def between_ranges(lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        answer = even_sum_even_odd(lower);
        if (answer == 1):
            print(str(lower) + " is an option");
        lower = int(lower + 1);

def even_sum_even_odd (num):
    num = int(num);
    sumE = int(0);
    sumO = int(0);
    while (num > 0):
        temp = int(num % 10);
        if (temp % 2 == 0):
            sumE = int(sumE + temp);
        else:
            sumO = int(sumO + temp);
        num = int(num / 10);
    if (sumE == sumO):
        return 1;
    else:
        return 0;


lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

between_ranges(lwr, upr);
input("\nDONE!\n")
