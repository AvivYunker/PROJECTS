# CREATED BY: Aviv Yunker
# NAME: "ASCII taxer function"
# TAGS: ASCII, taxer, function, no-return, print, while, if-elif
# EXPLANATION: this program will take a number - and will randomly select a random characrater
# and based on that - will print that character, while subtracting it's ASCII
# value from the original number - and this process will repeat till the original number
# turns into zero (or close to zero).
# in case that the original number is only close to zero - it will form an
# 'exhaust' (a character made from the remaining value of the original number)
# to really turn it this time into 0
# EXAMPLE
# 1000 --> (biebrwiqt,?)
import random
def between_ranges(lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        print(str(lower), end=" --> (");
        ASCII_taxer(lower);
        print(")");
        lower = int(lower + 1);

def ASCII_taxer (num):
    num = int(num);
    while (num > 0):
        rand = random.randrange(97,122);
        if (num >= rand):
            print(chr(rand), end="");
            num = int(num - rand);
        elif (num > 0 and num < 97):
            print("," + chr(num), end="");
            num = int(num - num);




lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
input("\nDONE!\n") # this holds the CLI.
