# CREATED BY: Aviv Yunker
# NAME: "inserts 'n' prime numbers into list"
# TAGS: prime, list, insert, function, while, if, return, print, 
# EXPLANATION: This program will insert 'n' prime numbers into a list,
# and then will print all of those numbers (from 0, till the count had
# been reached).
# EXAMPLE:
# input: 5.
# results: 2,3,5,7,11.
def prime_loader(num):
    num = int(num);
    arr = [];
    x = int(2);
    while (num > 0):
        results = is_prime(x);
        if (results == 1):
            arr.append(x);
            num = int(num - 1);
        x = int(x + 1);
    lim = len(arr);
    for cnt in range (0, lim, 1):
        print(str(arr[cnt]), end=",");

def is_prime(num):
    num = int(num);
    b = int(num - 1);
    while (b > 1):
        if (num % b == 0):
            return 0;
        b = int(b - 1);
    return 1;



x = input("User, how many prime numbers do you want to load?\n");
x = int(x);

prime_loader(x);
input("\nDONE!\n") # This holds the CLI.
