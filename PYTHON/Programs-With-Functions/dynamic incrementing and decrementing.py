# CREATED BY: Aviv Yunker
# NAME: "dynamic incrementing and decrementing"
# TAGS: dynamic, random, input, output, while, if-elif, logical-operators, os
# EXPLANATION: this program will keep asking for input, till the number is
# out of ranges
# EXAMPLE:
# [3]
# 'q' - increment
# 'a' - decrement
import random
import os
x = random.randrange(0,10)
while (x >= 0 and x <= 9):
    os.system('cls')
    print("[" + str(x) + "]", end="\n")
    key = input("User:\nQ - UP\nA - DOWN\n")
    key = str(key)
    if (key == 'q'):
        x = int(x + 1)
    elif (key == 'a'):
        x = int(x - 1)
    else:
        input(" 'q' or 'a' only!\n")
input("\nDONE!\n") # This holds the CLI.
