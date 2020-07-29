def power_function(base, power):
    base = int(base);
    power = int(power);
    sum = int(1);
    while (power > 0):
        sum = int(sum * base);
        power = int(power - 1);
    return sum;


x = input("User, enter the base:\n");
y = input("User, enter the power:\n");

x = int(x);
y = int(y);

results = power_function(x, y);
print("The results are: " + str(results));
input("DONE!\n");