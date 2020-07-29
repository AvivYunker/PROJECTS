def two_integer_sum (num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return (num1 + num2)

a = input("User, enter the first number:\n")
b = input("User, enter the second number:\n")

a = int(a)
b = int(b)

sums = two_integer_sum(a, b)
print("The sum of " + str(a) + " and of " + str(b) + " is: " + str(sums))
