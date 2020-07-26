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
	print("")

x = int(input("User, how many numbers? "))
fibonacci(x)
