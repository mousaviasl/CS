print("This program checks the properness of a proposed variable name.")
print()
print()
substring = " "
variable = input("Enter a variable name (q to quit): ")
while True:
    if variable == 'q':
        break
    if ' ' in variable:
        print("Illegal (no spaces allowed, must begin with a letter)")
    elif variable.isalnum() != True:
        print("legal, but uses poor style (should only use letters or digits)")
    elif variable.isalnum() == True:
        print("It is great!")
    variable = input("Enter another variable name (q to quit): ")
print("Finsihed! Have a great day!")