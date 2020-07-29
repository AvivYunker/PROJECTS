def dynamic_triangle(x):
    x = int(x)
    orig = int(x)
    a = int(x-1)
    b = '/'
    c = int(0)
    d = '|'
    e = int(x-1)
    aa = int(0)
    cc = int(0)
    while (x > 0 and x < 121):
        aa = a
        while (aa > 0):
            print(" ", end="")
            aa = int(aa - 1)

        a = int(a - 1)
        print(b, end="")
        cc = c
        if (x == 1):
            cc = 0
            while (e > 0):
                print("_", end="")
                e = int(e - 1)
        while (cc > 0):
            print(" ", end="")
            cc = int(cc - 1)
        c = int(c + 1)
        print(d)
        x = int(x - 1)
x = input("User, enter the height of the triangle, maximum 120:\n")
print("\n")
dynamic_triangle(x)
input("\nDONE!\n")
