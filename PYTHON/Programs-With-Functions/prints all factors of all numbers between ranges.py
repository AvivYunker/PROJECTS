# this program will (for each number) print all of it's divisors (excluding itself, including 1)
# TAGS: ranges, divisors, while, if, else, array, parenthesis
def between_ranges(lower, upper):
    print("\n");
    lower = int(lower);
    uppr = int(upper);
    while (lower <= upper):
        print(str(lower) + " --> ", end="");
        all_divisors(lower);
        lower = int(lower + 1);

def all_divisors (num):
    num = int(num);
    arr = [];
    if (num == 1):
        b = int(1);
    else:
        b = int(num - 1);
    while (b >= 1):
        if (num % b == 0):
            arr.append(b);
        b = int(b - 1);
    lim = len(arr);
    print("(", end="");
    for cnt in range (lim - 1, -1, -1):
        if (cnt == 0):
            print(arr[cnt], end="");
        else:
            print(arr[cnt], end=",");
    print(")");


lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
input("\nDONE!\n")
