def digit_sum (num):
    num = int(num);
    sum = int(0);
    while (num > 0):
        temp = int(num % 10);
        sum = int(sum + temp);
        num = int(num / 10);
    return sum;

x= input("User, enter a number:\n");
x = int(x);

results = digit_sum(x);
print("The sum of the digits is: " + str(results));
input("DONE!\n");