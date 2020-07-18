def main():
	lower = int(input("User, enter the lower edge: "))
	upper = int(input("User, enter the upper edge: "))
	while (lower <= upper):
		print(str(lower) + " --> " + str(chr(lower)))
		lower = int(lower + 1)


main()
