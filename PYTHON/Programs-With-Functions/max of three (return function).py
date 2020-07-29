def max_of_three (num1, num2, num3):
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    if ((num1 > num2) and (num1 > num3)):
        return num1
    elif ((num2 > num1) and (num2 > num3)):
        return num2
    elif ((num3 > num1) and (num3 > num2)):
        return num3
    else:
        print("\nERROR!\n")

a = input("User, enter the first number:\n")
b = input("User, enter the second number:\n")
c = input("User, enter the third number:\n")

a = int(a)
b = int(b)
c = int(c)

results = max_of_three(a, b, c)
print("\nThe results are: " + str(results))
input("\nDONE!\n")
