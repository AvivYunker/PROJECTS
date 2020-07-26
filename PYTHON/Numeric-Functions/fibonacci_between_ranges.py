def between_ranges(lower, upper):
	lower = int(lower)
	upper = int(upper)
	while (lower <= upper):
		print(str(lower), end=" --> (")
		fibonacci(lower)
		print(")")
		lower = int(lower + 1)

def fibonacci (num):
        num = int(num)
        num1 = int(0)
        num2 = int(1)
        while (num > 0):
                num2 = int(num2 + num1)
                num1 = int(num1 + num2)
                print(str(num2), end=",")
                num = int(num - 1)
                if (num > 0):
                        print(str(num1), end=",")
                        num = int(num - 1)


lwr = int(input("User, enter the lower edge: "))
upr = int(input("User, enter the upper edge: "))
between_ranges(lwr, upr)
