def between_ranges (lower, upper):
	lower = int(lower)
	upper = int(upper)
	while (lower <= upper):
		arr = []
		digits_to_array(arr, lower)
		results = is_palindrome(arr)
		if (results == int(1)):
			print(str(lower) + " is a palindrome")
		lower = int(lower + 1)

def digits_to_array (arr, num):
	num = int(num)
	while (num > 0):
		temp = int(num % 10)
		arr.append(temp)
		num = int(num / 10)

def is_palindrome (arr):
	cnt2 = int(len(arr)-1)
	for cnt1 in range(0, len(arr), 1):
		if (arr[cnt1] != arr[cnt2]):
			return 0
		cnt2 = int(cnt2 - 1)
	return 1

lwr = int(input("User, enter the lower edge: "))
upr = int(input("User, enter the upper edge: "))
between_ranges(lwr, upr)
