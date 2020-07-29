# CREATED BY: Aviv Yunker
# NAME: Basic calculator
# TAGS: calculator, basic, operators, operands, operations, input, output, if-elif, print, no-return
# EXPLANATION: This program will receive 2 integers - and a number that indicated the math operator -
# done on these 2 first entered numbers. The results will be the printed results of the math operation.
# EXAMPLE:
# 5 + 5 = 10

def basic_calculator (num1, num2, oper):
    num1 = int(num1)
    num2 = int(num2)
    oper = int(oper)

    if (oper == 1):
        print("\nThe results are: " + str(num1 + num2))
    elif (oper == 2):
        print("\nThe results are: " + str(num1 - num2))
    elif (oper == 3):
        print("\nThe results are: " + str(num1 * num2))
    elif (oper == 4):
        print("\nThe results are: " + str(num1 / num2))
    elif (oper == 5):
        print("\nThe results are: " + str(num1 % num2))
    else:
        print("ERROR! ivalid operator.")


a = input("User, enter the first integer:\n")
b = input("User, enter the second integer:\n")
c = input("User, select one of the followings:\n1 - Addition (+)\n2 - Subtraction (-)\n3 - Multiplication (*)\n4 - Division (/)\n5 - Modulus (%)\n")

a = int(a)
b = int(b)
c = int(c)

basic_calculator(a, b, c)
input("\nDONE!\n") # This holds the CLI.
