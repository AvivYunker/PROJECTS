def str_rchr (strr, chrr):
	res = int(0)
	if (len(chrr) != 1):
		print("ERROR! Not a single character!")
		return -1
	else:
		for i in range(0, len(strr), 1):
			if (strr[i] == chrr):
				res = int(i)
	return res+1 # +1 for human readability (so it won't start at 0).

strr = input("User, enter a string: ")
chrr = input("User, enter the char: ")
last = str_rchr(strr, chrr)
print("Results: " + str(last))
