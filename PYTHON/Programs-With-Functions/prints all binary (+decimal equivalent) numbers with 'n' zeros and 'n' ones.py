def binary_infinitely (zeros, ones):
    zeros = int(zeros); #V
    ones = int(ones); #V
    cntZero = int(0);
    cntOne = int(0);
    decimal = int(1);
    x = decimal_to_binary(decimal);
    d = digit_counter(x);
    while (d <= int(zeros + ones)):
        while (x > 0):
            temp = int(x % 10);
            if (temp == 1):
                cntOne = int(cntOne + 1);
            else:
                cntZero = int(cntZero + 1);
            x = int(x / 10);
        if (cntZero == zeros and cntOne == ones):
            print(str(decimal_to_binary(decimal)), end=" --> (");
            print(str(decimal) + ")");
        decimal = int(decimal + 1);
        cntOne = int(0);
        cntZero = int(0);
        x = decimal_to_binary(decimal);
        d = digit_counter(x);




def decimal_to_binary (num):
    num = int(num);
    res = int(0);
    level = int(1);
    while (num > 0):
        tempI = int(num / 2);
        tempF = float(num*1.0 / 2);
        tempF = float(tempF - tempI);
        tempF = int(tempF * 2);
        res = int(res + tempF*level);
        level = int(level * 10);
        num = int(tempI);
    return res

def binary_to_decimal (num):
    num = int(num);
    res = int(0);
    level = int(1);
    while (num > 0):
        temp = int(num % 10);
        temp = temp * pow(2, level);
        sums = int(sums + temp);
        level = int(level + 1);
        num = int(num / 10);
    return sums;

def digit_counter (num):
    num = int(num);
    counter = int(0);
    if (num == 0):
        counter = int(1);
    else:
        while (num > 0):
            counter = int(counter + 1);
            num = int(num / 10);
    return counter;

zrs = input("User, how many zeros?\n");
ons = input("User, how many ones?\n");

zrs = int(zrs);
ons = int(ons);

binary_infinitely(zrs, ons);
input("DONE!");
