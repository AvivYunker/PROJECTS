# CREATED BY: Aviv Yunker
# NAME: "Armstrong numbers for each number till zero"
# TAGS: Armstrong, ranges, while, if, if-else, digit-counter, digit, function, return
# EXPLANATION: for each number in between ranges - it will print all Armstrong numbers
# from this number, down to 0.
# EXAMPLE:
# 1000 --> 0,1,2,3,4,5,6,7,8,9,153,370,371,407
def between_ranges (lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        print(str(lower), end=" --> (");
        armstrong_till_zero(lower);
        print(")");
        lower = int(lower + 1);

def armstrong_till_zero (num):
    num = int(num);
    pr = int(num);
    lw = int(0);
    while (lw <= pr):
        tempLw = int(lw);
        sums = int(0);
        d = digit_counter(tempLw);
        while (tempLw > 0):
            temp = int(tempLw % 10);
            temp = pow(temp, d);
            sums = int(sums + temp);
            tempLw = int(tempLw / 10);
        if (sums == lw):
            if (sums == 0):
                print(str(lw), end="")
            else:
                print("," + str(lw), end="");
        lw = int(lw + 1);

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
input("DONE!\n"); # This holds the CLI.
