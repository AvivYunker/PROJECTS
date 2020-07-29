import random
def n_random_ip_addresses (num):
    num = int(num);
    while (num > 0):
        for cnt in range(0, 4, 1):
            segmt = random.randrange(0,255);
            if (cnt < 3):
                print(str(segmt), end=".");
            else:
                print(str(segmt));
        num = int(num - 1);



x = input("User, how many IP addresses?  ");

n_random_ip_addresses(x);
input("\nDONE!\n")