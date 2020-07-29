# this program produces 'n' IP addresses randomly
# TAGS: IP, random, address, randrange,
import random

def n_random_ip_add(x):
    for cnt1 in range (0, x, 1):
        for cnt2 in range (0, 4, 1):
            for cnt3 in range (0, 8, 1):
                digit = random.randrange(0,2);
                print(digit, end="");
            if(cnt2 == 3):
                 print("");
            else:
                 print(".", end="");
        print("");

x = input("User, enter number of random IP addresses:\n");
x = int(x);

n_random_ip_add(x);
input("\nDONE!\n")
