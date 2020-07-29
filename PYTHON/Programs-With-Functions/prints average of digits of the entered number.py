def avg_digits (num):
    num = int(num);
    d = digit_counter(num);
    sums = int(0);
    while (num > 0):
        temp = int(num % 10);
        sums = int(sums + temp);
        num = int(num / 10);
    avg = float(sums*1.0 / d);
    return avg;
def digit_counter(x):
    x = int(x);
    counter = int(0);
    if (x == 0):
        counter = int(1);
    else:
        while (x > 0):
            counter = int(counter + 1);
            x = int(x / 10);
    return counter;

x = input("User, enter a number:\n");
x = int(x);

results = avg_digits(x);
print("The average of digits is: " + str(results));
input("DONE!\n");