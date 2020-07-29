# 1234 --> 10 --> 1111001100 --> 972
import random
def digit_counter (num):
    num = int(num)
    res = int(0)
    while (num > 0):
        temp = int(num % 10)
        res = int(res + temp)
        num = int(num / 10)
    return res

def randomized_binary_by_digits (dig_select):
    dig_select = int(dig_select)
    res = int(0)
    level = int(1)
    while (dig_select > 0):
        rndm = random.randrange(0, 2)
        temp = int(rndm * level)
        res = int(res + temp)
        level = int(level * 10)
        dig_select = int(dig_select - 1)
    return res

def binary_to_decimal (num):
    num = int(num);
    sum = int(0);
    level = int(0);
    while (num > 0):
        temp = int(num % 10);
        temp = int(temp * pow(2,level));
        sum = int(sum + temp);
        level = int(level + 1);
        num = int(num / 10);
    return sum;


x = input("User, enter a number:\n")
x = int(x)
print("(" + str(x), end=") --> (")
sum_d = digit_counter(x)
print(str(sum_d), end = ") --> (")
num_bin = randomized_binary_by_digits(sum_d)
print(str(num_bin), end = ") --> (")
dec_cnvt = binary_to_decimal(num_bin)
print(str(dec_cnvt) + ")")
input("\nDONE!\n")