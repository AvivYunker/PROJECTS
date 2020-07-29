# this program will print 'n' alphabet letters
# TAGS: alphabet, letters, number, first, print
def n_letters_abc (num):
    print("\n");
    num = int(num);
    x = int(65);
    if (num > 26):
        print("ERROR!\n")
    else:
        while (num > 0):
            print(chr(x), end=", ");
            x = int(x + 1);
            num = int(num - 1);
        print("\n");

x = input("User, how many letters?\n")
x = int(x);

n_letters_abc(x);
input("\nDONE!\n")
