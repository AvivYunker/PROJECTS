# this program will print 'n' binary IP addresses, along with their conversion to decimal in the same line
# TAGS: IP address, random, randrange, arrays, if, elif, for, input, decimal, binary, convert, conversion
import random
def n_random_ip_addresses (num):
    num = int(num);
    for cnt1 in range (0, num, 1):
        arr1 = [];
        arr2 = [];
        arr3 = [];
        arr4 = [];
        for cnt2 in range (0, 4, 1):
            sum = int(0);
            for cnt3 in range (0, 8, 1):
                digit = random.randrange(0,2);
                if (cnt2 == 0):
                    arr1.append(digit);
                elif (cnt2 == 1):
                    arr2.append(digit);
                elif (cnt2 == 2):
                    arr3.append(digit);
                elif (cnt2 == 3):
                    arr4.append(digit);
                print(digit, end="");
            if (cnt2 == 3):
                print("", end="");
            else:
                print(".", end="");
        print("  --->  (", end="");
        for cnt4 in range (0, 4, 1):
            if (cnt4 == 0):
                print(binary_to_decimal(arr1), end="");
            elif (cnt4 == 1):
                print(binary_to_decimal(arr2), end="");
            elif (cnt4 == 2):
                print(binary_to_decimal(arr3), end="");
            elif (cnt4 == 3):
                print(binary_to_decimal(arr4), end="");
            if (cnt4 < 3):
                print(".", end="");
            else:
                print(")\n", end="");
    print("\n");

def binary_to_decimal (num):
    sum = int(0);
    power = int(0);
    lim = len(num);
    #print("\n//" + str(lim) + "//\n");
    for cnt in range (lim - 1, -1, -1):
        #print("\n//" + str(num[cnt]) + "//\n");
        temp = num[cnt];
        thePower = int(pow(2, power));
        temp = int(temp*thePower);
        sum = int(sum + temp);
        power = int(power + 1);
    return sum;


x = input("User, how many random IP addresses:  ");
x = int(x);

n_random_ip_addresses(x);
input("\nDONE!\n")
