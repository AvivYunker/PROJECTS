# this program will print all the numbers of product 'x' ('x' is input) in between ranges
# TAGS: product, ranges,
def between_ranges(lower, upper):
    print("\n");
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        results = is_prod(lower, prod);
        if (results == 1):
            print(str(lower) + " is an option");
        lower = int(lower + 1);

def is_prod (num, product):
    num = int(num);
    product = int(product);
    sum = int(1);
    while (num > 0):
        temp = int(num % 10);
        sum = int(sum * temp);
        num = int(num / 10);
    if (sum == product):
        return 1;
    else:
        return 0;

lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");
prod = input("User, enter the product:\n");

lwr = int(lwr);
upr = int(upr);
prod = int(prod);

between_ranges(lwr, upr);
input("\nDONE!\n")

