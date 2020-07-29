# CREATED BY: Aviv Yunker
# NAME: "Binary number boggler"
# TAGS: binary, digit, boggler, function, return, if-else, while, or, 
# EXPLANATION: this program will access an input - and then print a random
# binary number with an equal number of '1' digits. The program will also
# convert the result binary number to a decimal number.
# EXAMPLE:
# input 1111 --> output: 1001101 --> 77.

import random
def binary_digit_boggle (num):
    num = int(num);
    cnt1 = int(0);
    cnt0 = int(0);
    sums = int(0);
    level = int(1);
    while (num > 0):
        temp = int(num % 10);
        if (temp == 1):
            cnt1 = int(cnt1 + 1);
        else:
            cnt0 = int(cnt0 + 1);
        num = int(num / 10);
    #print("cnt1=" + str(cnt1) + " / cnt0=" + str(cnt0));
    while (cnt1 > 0 or cnt0 > 0):
        rand = random.randrange(0,2);
        #print(str(rand));
        if (rand == 0 and cnt0 > 0):
            sums = int(sums + rand*level);
            cnt0 = int(cnt0 - 1);
        elif (rand == 1 and cnt1 > 0):
            sums = int(sums + rand*level);
            cnt1 = int(cnt1 - 1);
        level = int(level * 10);
    print(str(sums), end=" ---> ");
    res = binary_to_decimal(sums);
    return res;

def binary_to_decimal (num):
    num = int(num);
    level = int(0);
    res = int(0);
    while (num > 0):
        temp = int(num % 10);
        res = int(res + temp * pow(2, level));
        num = int(num / 10);
        level = int(level + 1);
    return res;


x = input("User, enter a binary number:\n");
x = int(x);

results = binary_digit_boggle(x);
print("The boggle results are: " + str(results));
input("\nDONE!\n") # This holds the CLI.
