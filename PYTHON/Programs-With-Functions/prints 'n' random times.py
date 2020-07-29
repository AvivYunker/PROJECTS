import random
def n_random_times (num):
    num = int(num);
    while (num > 0):
        hours = random.randrange(0,24);
        minutes = random.randrange(0,59);
        if (hours < 10):
            print("0", end="");
        print(str(hours), end=":");
        if (minutes < 10):
            print("0", end="");
        print(str(minutes), end="");
        if (hours <= 11):
            print("   (AM)");
        else:
            print("   (PM)");
        num = int(num - 1);




x = input("User, how many random times?\n");
x = int(x);
print("\n");
n_random_times(x);
input("DONE!\n");