# CREATED BY: Aviv Yunker
# NAME: "even and odd digit counter"
# TAGS: even, odd, counter, digits, while, if-else, function, no-return, print
# EXPLANATION: this program will print the number of even and of odd digits in
# the entered number, without returning them.
# EXAMPLE:
# input 12345 - even:2, odd:3
def even_odd_counter (num):
    num = int(num);
    cntE = int(0);
    cntO = int(0);
    while (num > 0):
        temp = int(num % 10);
        if (temp % 2 == 0):
            cntE = int(cntE + 1);
        else:
            cntO = int(cntO + 1);
        num = int(num / 10);
    print("number of even digits: " + str(cntE));
    print("number of odd digits: " + str(cntO));


x = input("User, enter a number:\n");
x = int(x);

even_odd_counter(x);
input("\nDONE!\n"); # This holds the CLI.
