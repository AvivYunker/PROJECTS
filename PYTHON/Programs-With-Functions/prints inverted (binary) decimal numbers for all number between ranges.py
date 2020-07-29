def between_ranges (lower, upper):
    lower = int(lower)
    upper = int(upper)
    while (lower <= upper):
        print(str(lower), end=" --> BIN:(")
        binary_orig = decimal_to_binary(lower)
        print(str(binary_orig), end=") --> BIN_INV:(")
        binary_inv = binary_inverter(binary_orig)
        print(str(binary_inv), end=") --> DEC_INV:(")
        decimal_inv = binary_to_decimal(binary_inv)
        print(str(decimal_inv) + ")")
        lower = int(lower + 1)

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

def binary_inverter (num):
    num = int(num)
    arrOrig = []
    arrInv = []
    digits_to_array(num, arrOrig)
    digit_inverter(arrOrig, arrInv)
    res = array_to_number(arrInv, num)
    return res

def digits_to_array (num, arrOrig):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arrOrig.append(temp)
        num = int(num / 10)
    lim = len(arrOrig)

def digit_inverter (arrOrig, arrInv):
    lim = len(arrOrig)
    for cnt in range(0, lim, 1):
        val = int(1 - arrOrig[cnt])
        arrInv.append(val)

def array_to_number (arrInv, num):
    num = int(0)
    lim = len(arrInv)
    level = int(1)
    for cnt in range(0, lim, 1):
        num = int(num + level * arrInv[cnt])
        level = int(level * 10)
    return num

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)
input("\nDONE!\n")
