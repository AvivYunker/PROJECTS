def sand_watch_printer (num):
    num = int(num);
    space = int(0);
    while (num > 0):
        tempSpace = int(space);
        tempNum = int(num);
        while (tempSpace > 0):
            print(" ", end="");
            tempSpace = int(tempSpace - 1);
        while (tempNum > 0):
            print("*", end="");
            tempNum = int(tempNum - 1);
        num = int(num - 1);
        space = int(space + 1);
        print("");



x = input("User, enter the base of the sand-watch ");
x = int(x);

sand_watch_printer(x);
input("DONE!\n");