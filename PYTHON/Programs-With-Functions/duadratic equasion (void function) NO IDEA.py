# NAME: "quadratic equasion"
# TAGS: quadratic, equasion, input, output, function, no-return, if-else, print
# EXPLANATION: this program will receive 3 parameters - and will print the results
# of the duadratic equasion
# EXAMPLE:
# input: a=3, b=4, c=1
# results: res1 = -1, res2 = -0.333

def quadratic_equasion (a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    root = float(pow(b*b -4*a*c, 0.5))
    x1 = float((-b + root)*1.0 / 2*a)
    x2 = float((-b - root)*1.0 / 2*a)
    if (x1 == x2):
        print("\nOne result: " + str(x1))
    else:
        print("\nTwo results: " + str(x1) + " and " + str(x2))


num1 = input("User, enter parameter 'a':\n")
num2 = input("User, enter parameter 'b':\n")
num3 = input("User, enter parameter 'c':\n")

num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

quadratic_equasion(num1, num2, num3)
input("\nDONE!\n")
