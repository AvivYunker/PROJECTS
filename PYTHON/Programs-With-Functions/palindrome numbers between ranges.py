def between_ranges(lower, upper):
    lower = int(lower);
    upper = int(upper);
    while (lower <= upper):
        results = is_palindrome(lower);
        if (results == 1):
            print(str(lower) + " is a palindrome");
        lower = int(lower + 1);

def is_palindrome (num):
    num = int(num);
    arr = [];
    while (num > 0):
        temp = int(num % 10);
        arr.append(temp);
        num = int(num / 10);
    lim = len(arr);
    cnt2 = int(lim-1);
    for cnt1 in range (0, lim-1, 1):
        if (arr[cnt1] != arr[cnt2]):
            return 0;
        cnt2 = int(cnt2 - 1);
    return 1;

lwr = input("User, enter the lower edge:\n");
upr = input("User, enter the upper edge:\n");

lwr = int(lwr);
upr = int(upr);

between_ranges(lwr, upr);
print("DONE!\n");
