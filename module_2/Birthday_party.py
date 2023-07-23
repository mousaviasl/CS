total = 0

while True:
    print("""Welcome to the Dinosaur Park Party Planner
    Choose the type of party
    1. General Group Rate Admission Party
    2. Bare Bones Package
    3. Deluxe Party Package
    4. Quit""")
    print("")

    choice = int(input("Enter your choice: "))
    print("")

    if choice == 4:
        print("Thank you for using the Dinosaur Park Party Planner.")
        break

    membership = int(input("Are you a member? Press 1 for yes and 2 for no: "))
    print("")
    print("The base cost covers admission for up to 12 people.  Enter in the amount of additional people: ")
    print("")
    add_adult = int(input("Number of additional adults: "))
    print("")
    add_children = int(input("Number of additional children: "))
    print("")

    if choice == 1:
        total = add_adult * 5.00 + add_children * 4.00 + 100.00
    elif choice == 2:
        if membership == 1:
            total = 99.00 + add_adult * 3.00 + add_children * 3.00
        elif membership == 2:
            total = 119.00 + add_adult * 3.00 + add_children * 3.00
    elif choice == 3:
        if membership == 1:
            total = 175.00 + add_adult * 3.00 + add_children * 3.00
        elif membership == 2:
            total = 199.00 + add_adult * 3.00 + add_children * 3.00

    print(f'Your total cost is: ${total}')
    print("")
