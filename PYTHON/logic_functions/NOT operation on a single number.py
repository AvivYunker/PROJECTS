# 18 --> 10010 --> 01101 --> 13
def NOT(num):
    num = int(num)
    bin_orig = decimal_to_binary(num)
    invert_bin = not_binary(bin_orig)
    invert_dec = binary_to_decimal(invert_bin)
    return invert_dec


def decimal_to_binary (num):
    num = int(num);
    sum = int(0);
    pusher = int(1);
    while (num > 0):
        temp = int(num % 2);
        sum = int(sum + temp * pusher);
        num = int(num / 2);
        pusher = int(pusher * 10);
    return sum;

def not_binary (num):
    num = int(num)
    level = int(1)
    res = int(0)
    while (num > 0):
        temp = int(num % 10)
        temp = int(1 - temp)
        res = int(res + temp * level)
        level = int(level * 10)
        num = int(num / 10)
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

z = NOT(x)
print("The results are: " + str(z))
input("\nDONE!\n")
