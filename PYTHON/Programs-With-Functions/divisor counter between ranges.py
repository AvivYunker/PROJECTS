# CREATED BY: Aviv Yunker
# NAME: "divisor counter between ranges"
# TAGS: divisor, counter, ranges, while, if, return, function
# EXPLANATION: for each number between ranges - it will print the number
# of divisors that this number has (the whole-divisors).
# EXAMPLES:
# 100 --> divisors are: 100,50,25,20,10,5,4,2,1 --> 9 divisors (results)
def between_ranges (lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        print(str(lower), end=" ---> (");
        print(str(divisor_counter(lower)) + " divisors", end="");
        print(")");
        lower = int(lower + 1);
    print("\nDONE!\n");

def divisor_counter (num):
    num = int(num);
    counter = int(0);
    b = int(num);
    while (b >= 1):
        if (num % b == 0):
            counter = int(counter + 1);
        b = int(b - 1);
    return counter;



lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
input("\nDONE!\n"); # This holds the CLI.
