# CREATED BY: Aviv Yunker
# NAME: "Basic printer"
# TAGS: basic, printer, function, no-return
def basic_printer (strr):
    strr = str(strr)
    print("Hi there, " + str(strr) + ".")

x = input("User enter your name:\n")
x = str(x)

basic_printer(x)
input("\nDONE!\n") # This holds the CLI.
