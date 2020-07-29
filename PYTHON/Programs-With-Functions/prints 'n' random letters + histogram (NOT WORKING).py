import random
def n_random_letters (num):
    num = int(num);
    arr = [0]*26;
    while (num > 0):
        letter = random.randrange(97,122);
        copyLetter = int(letter - 97);
        val = int(arr[copyLetter]);
        arr.insert(copyLetter, val + 1);
        print(chr(letter), end="");
        num = int(num - 1);
    print("\n");
    for cnt1 in range (0, 25, 1):
        if (arr[cnt1] > 0):
            print(chr(cnt1 + 97), end=": (");
            for cnt2 in range (0, arr[cnt1], 1):
                print("*", end="");
            print(")");
    print("FINISHED!");


x = input("User, how many random letters?\n");
x = int(x);
n_random_letters(x);
input("\n\nDONE!");
