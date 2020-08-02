def str_len (strr):
	res = int(0)
	i = int(0)
	stop = int(0)
	while (stop == int(0)):
		try:
			if (strr[i]):
				i += 1
		except:
			stop = int(1)
	return i

x = input("User, enter a string: ")
results = str_len(x)
print(str(x) + " has " + str(results) + " characters.")
