# CREATED BY: Aviv Yunker
# NAME: Asterisk scale of 'n' random digits
# TAGS: Asterisk, scale, random, digit, while, for-loop, if-else, print
# EXPLANATION: this program will print an asterisk scale for each randomized digit
# till the count of number has been reached. The asterisk scale is similar to what
# could be found in blood-tests. The scale range is from 0 to 9.
# EXAMPLE:
# 5 - (_____*____)
# 2 - (__*_______)

import random
def n_random_numbers(num):
    num = int(num)
    while (num > 0):
        rnd = random.randrange(0, 10)
        print(str(rnd), end=" --> (")
        asterisk_scale(rnd)
        print(")")
        num = int(num - 1)

def asterisk_scale (num):
    num = int(num)
    arr = [0]*10
    lim = len(arr)
    for cnt1 in range(0, lim, 1):
        if (num == cnt1):
            print("*", end="")
        else:
            print("_", end="")

num = input("User, how many numbers?\n")
num = int(num)

n_random_numbers(num)
input("DONE!\n") # This holds the CLI.
