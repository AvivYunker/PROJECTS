# CREATED BY: Aviv Yunker
# NAME: "compare 2 integers"
# TAGS: compare, integers, return, function, if-elif, input, output
# EXPLANATION: for each 2 integers entered - it will return the largest integer (similar to strcmp function)
# EXAMPLE:
# 100 and 10 --> 100 is greater than 10
# 50 and 50 --> 50 is equal to 50
# 30 and 400 --> 30 is lesser than 400
def compare_two_integers (num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if (num1 > num2):
        return 1
    elif (num1 == num2):
        return 0
    elif (num1 < num2):
        return -1

a = input("User, enter the first number:\n")
b = input("User, enter the second number:\n")

a = int(a)
b = int(b)

results = compare_two_integers(a, b)
if (results == 1):
    print(str(a) + " is greater than " + str(b)
elif (results == 0):
    print(str(a) + " is equal to " + str(b))
elif (results == -1):
    print(str(a) + " is lesser than " + str(b))
input("\nDONE!\n") # This holds the CLI.
