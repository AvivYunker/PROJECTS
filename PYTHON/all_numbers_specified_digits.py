def all_numbers_digits (dig):
	dig = int(dig)
	lower = int(pow(10,dig-1))
	upper = int(pow(10,dig)-1)
	while (lower <= upper):
		print(str(lower), end=",")
		lower = int(lower + 1)
	print("")

x = int(input("User, enter a number: "))
all_numbers_digits(x)
