def str_chr (arr, strr, chrr):
	for i in range(0, len(strr), 1):
		#print("strr: " + strr[i])
		#print("chrr: " + chrr)
		if(strr[i] == chrr):
			arr.append(int(i+1))

strr = input("User, enter a string: ")
chrr = input("User, enter the character: ")
arr = []
str_chr(arr, strr, chrr)

print("the char: " + str(chrr) + " was found at: ")
for cnt in range(0, len(arr), 1):
	print(str(arr[cnt]), end=",")
print("")
