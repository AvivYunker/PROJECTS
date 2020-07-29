def ASCII_between_ranges(lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        print(str(lower) + " ---> " + chr(lower));
        lower = int(lower + 1);

lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

ASCII_between_ranges(lwr, upr);
input("\nDONE!\n")