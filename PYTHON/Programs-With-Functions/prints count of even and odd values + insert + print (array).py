def insert_into_array (x, arr):
    x = int(x)
    for cnt in range(0, x, 1):
        val = input("User, enter value for cell no. " + str(cnt + 1) + "  ")
        val = int(val)
        arr.append(val)

def even_odd_counter_array (arr):
    cntE = int(0)
    cntO = int(0)
    lim = len(arr)
    print("")
    for cnt in range(0, lim, 1):
        if (arr[cnt] % 2 == 0):
            cntE = int(cntE + 1)
        else:
            cntO = int(cntO + 1)
    print("There are: " + str(cntE) + " even values.")
    print("There are: " + str(cntO) + " odd values.")

def print_array_contents (arr):
    lim = len(arr)
    print("")
    for cnt in range(0, lim, 1):
        print(str(arr[cnt]), end=",")

x = input("User, array size?\n")
x = int(x)
arr = []

insert_into_array(x, arr)
even_odd_counter_array(arr)
print_array_contents(arr)
