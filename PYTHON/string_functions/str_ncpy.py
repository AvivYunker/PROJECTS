def str_ncpy (str1, str2, num):
	num = int(num)
	for i in range(0, num, 1):
		str2 += str1[i]
	return str2

str1 = input("User, enter a string: ")
str2 = str("")
num = int(input("User, enter the number: "))

str2 = str_ncpy(str1,str2,num)
print("The second string is: " + str(str2))
