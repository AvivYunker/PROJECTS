import random
def n_random_numbers (num):
    num = int(num);
    arr = [0]*10;
    while (num > 0):
        rand = random.randrange(0, 1000);
        digit_histogram(rand, arr);
        print(str(rand));
        num = int(num - 1);
    for cnt1 in range(0, 10, 1):
        print(str(cnt1), end=" ---> (");
        for cnt2 in range(0, arr[cnt1], 1):
            print("*", end="");
        print(")");

def digit_histogram(num, arr):
    num = int(num);
    while (num > 0):
        temp = int(num % 10);
        val = int(arr[temp] + 1);
        arr.insert(temp, val);
        num = int(num / 10);


x= input("User, how many random numbers:\n");
x = int(x);

n_random_numbers(x);