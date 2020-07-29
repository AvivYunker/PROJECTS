def between_ranges (lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        print(str(lower), end=" --> ");
        evenOdd_digit_counter(lower);
        lower = int(lower + 1);

def evenOdd_digit_counter (num):
    num = int(num);
    cntE = int(0);
    cntO = int(0);
    while (num > 0):
        temp = int(num % 10);
        if (temp % 2 == 0):
            cntE = int(cntE + 1);
        else:
            cntO = int(cntO + 1);
        num = int(num / 10);
    print("even:" + str(cntE) + " / odd:" + str(cntO));

lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
input("\nDONE!\n")