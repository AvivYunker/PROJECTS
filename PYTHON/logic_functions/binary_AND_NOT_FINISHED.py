def decimal_to_binary (num):
	num = int(num)
	res = int(0)
	level = int(1)
	while (num > 0):
		tempI = int(num / 2)
		tempF = float(num / 2.0)
		tempF = float(tempF - tempI)
		tempF = int(tempF * 2)
		res = int(res + tempF * level)
		level = int(level * 10)
		num = int(tempI)
	return res

def digits_to_array (arr, num):
	num = int(num)
	while (num > 0):
		temp = int(num % 10)
		arr.append(temp)
		num = int(num / 10)

def length_equalizer (arr1, arr2):
	len1 = len(arr1)
	len2 = len(arr2)
	if (len1 >= len2):
		for cnt in range(0, len1-len2, 1):
			arr2.append(0)
	else:
		for cnt in range(0, len2-len1, 1):
			arr1.append(0)

def array_reverse(arr_new, arr_old):
	for cnt in range(len(arr_old)-1, -1, -1):
		arr_new.append(arr_old[cnt])

def AND_two_arrays (arr_res, arr1, arr2):
	length = len(arr1)
	for cnt in range(0, len(arr1), 1):
		arr_res.append(arr1[cnt] * arr2[cnt])

def array_to_number (num, arr):
	level = int(1)
	for cnt in range(0, len(arr), 1):
		num = int(num + arr[cnt] * level)
		level = int(level * 10)
	return num

def binary_to_decimal (dec_num, bin_num):
	bin_num = int(bin_num)
	level = int(1)


n1_dec = int(input("User, enter the first number: "))
n2_dec = int(input("User, enter the second number: "))

n1_bin = decimal_to_binary(n1_dec)
n2_bin = decimal_to_binary(n2_dec)

n1_bin_array = []
n2_bin_array = []

n1_bin_array_rev = []
n2_bin_array_rev = []

and_array = []
and_array_rev = []
bin_res = int(0)
dec_res = int(0)

digits_to_array(n1_bin_array, n1_bin)
digits_to_array(n2_bin_array, n2_bin)

array_reverse(n1_bin_array_rev, n1_bin_array)
array_reverse(n2_bin_array_rev, n2_bin_array)

for cnt in range(0, len(n1_bin_array_rev), 1):
	print(n1_bin_array_rev[cnt], end=",")
print("")
for cnt in range(0, len(n2_bin_array_rev), 1):
	print(n2_bin_array_rev[cnt], end=",")
print("\n")

length_equalizer(n1_bin_array_rev, n2_bin_array_rev)

for cnt in range(0, len(n1_bin_array_rev), 1):
        print(n1_bin_array_rev[cnt], end=",")
print("")
for cnt in range(0, len(n2_bin_array_rev), 1):
        print(n2_bin_array_rev[cnt], end=",")
print("\n")

AND_two_arrays (and_array, n1_bin_array_rev, n2_bin_array_rev)

for cnt in range(0, len(and_array), 1):
	print(and_array[cnt], end=",")
print("\n")

array_reverse(and_array_rev, and_array)

bin_res = array_to_number(bin_res, and_array_rev)

dec_res = binary_to_decimal (dec_res, bin_res)

print("The results are: " + str(dec_res))
