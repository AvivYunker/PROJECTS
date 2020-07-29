# this program will calculate sum of digits for every number between the entered ranges
# TAGS: ranges, sum, digits,
def between_ranges(lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        results = sum_digits(lower);
        print(str(lower) + " --> " + str(results));
        lower = int(lower + 1);

def sum_digits(num):
    num = int(num);
    sum = int(0);
    while (num > 0):
        temp = int(num % 10);
        sum = int(sum + temp);
        num = int(num / 10);
    return sum;

lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
input("\nDONE!\n")
