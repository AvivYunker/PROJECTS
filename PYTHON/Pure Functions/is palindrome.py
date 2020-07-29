def is_palindrome (num):
    num = int(num)
    arr = []
    digits_to_array(arr, num)
    lim = len(arr)
    cnt2 = int(lim-1)
    for cnt1 in range(0, lim, 1):
        if (arr[cnt1] != arr[cnt2]):
            return 0
        cnt2 = int(cnt2 - 1)
    return 1

def digits_to_array (arr, num):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arr.append(temp)
        num = int(num / 10)

x = input("User, enter a number:\n")
x = int(x)

results = is_palindrome(x)
if (results == 1):
    print("Is palindrome")
else:
    print("Is NOT palindrome")
input("\nDONE!\n")