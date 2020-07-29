def asterisks_to_ASCII (num):
    for cnt1 in range (0, int(num), 1):
        for cnt2 in range (0, int(num), 1):
            print("*", end="");
        print("");

x = input("User, enter some char:\n");
asterisks_to_ASCII(x);
