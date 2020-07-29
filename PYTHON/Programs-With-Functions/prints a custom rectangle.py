# this program prints a custom triangle - with accordance to no. of rows and of columns
# TAGS: rows, columns, cols, print, asterisks, custom, rectangle, shape
def custom_rectangle(ROW, COL):
    ROW = int(ROW);
    COL = int(COL);
    for cnt1 in range (0, ROW, 1):
        for cnt2 in range (0, COL, 1):
            print("*", end="");
        print("");

row = input("User, enter number of rows:\n");
col = input("User, enter number of columns:\n");

row = int(row);
col = int(col);

custom_rectangle(row, col);
