import random
def random_digits_to_array(arr, num):
    num = int(num)
    while (num > 0):
        dig = random.randrange(0, 10)
        arr.append(dig)
        num-=1

def percent_histogram (arr):
    lim = len(arr)
    arr_cnt = []
    for dig in range(0, 10):
        arr_cnt.append(arr.count(dig))
    lim_cnt = len(arr_cnt)
    for cnt in range(0, 10, 1):
        print(str(cnt), end=" --> (")
        tmp = arr_cnt[cnt]/lim
        tmp*= 100
        print(str(int(tmp)) + "%)")


x = input("User, how many random digits?\n")
x = int(x)
arr = []
random_digits_to_array(arr, x)
percent_histogram(arr)
input("\nDONE!\n")