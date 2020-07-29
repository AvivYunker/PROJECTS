# CREATED BY: Aviv Yunker
# NAME: Factor Histogram between ranges
# TAGS: factor, histogram, asterisk,ranges, while, if-else, for-in, digits, print, not-return, functions,
# EXPLANATION: this program will run in between specified ranges. For each number in
# between these ranges - it will perform a factor between all of it's digit,
# and then will print a number of asterisks, which matches the results of the factor
# between the digits.
# EXAMPLE:
# 123 --> 1 * 2 * 3 = 6 --> will print 6 asterisks

def between_ranges (lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        print(str(lower),end=" --> (");
        basic_factor_histogram(lower)
        print(")");
        lower = int(lower + 1);

def basic_factor_histogram (num):
    num = int(num);
    factor = int(1);
    if (num == 0):
        factor = int(0);
    else:
        while (num > 0):
            temp = int(num % 10);
            factor = int(factor * temp);
            num = int(num / 10);
    for cnt in range (0, factor, 1):
        print("*", end="");


lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
input("DONE!\n"); # this holds the CLI.
