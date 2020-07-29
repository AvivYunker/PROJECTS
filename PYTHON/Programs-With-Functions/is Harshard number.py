# CREATED BY: Aviv Yunker
# NAME: "is Harshard number"
# TAGS: harshard, numeric, while, for-in, function, return, print, if-else
# EXPLANATION: This program receives a number - and determines if the number
# is Harshard or not. A Harshard number is a number that can be divided by
# the sum of it's digits.
# EXAMPLE:
# 12 --> 6,3,2,1 --> 6+3+2+1 = 12. 12 is dividable by 12. 12 is a Harshard number.
# 20 --> 10,5,4,2,1 --> 10+5+4+2+1 = 22. 20 is NOT vidiable by 22. 22 is NOT a Harshard number.
def is_harshard (num):
    num = int(num)
    arr = []
    digits_to_array(num, arr)
    sumD = digit_summer(arr)
    if (num % sumD == 0):
        return 1
    else:
        return 0

def digits_to_array (num, arr):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

def digit_summer(arr):
    res = int(0)
    lim = len(arr)
    for cnt in range(0, lim, 1):
        res = int(res + arr[cnt])
    return res

x = input("User, enter a number:\n")
x = int(x)
results = is_harshard(x)
if (results == 1):
    print(str(x) + " is a Harshard number")
else:
    print(str(x) + " is NOT a Harshard number")
input("\nDONE!\n") # This holds the CLI.
