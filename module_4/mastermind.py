import random
numbers = []
assumptions = []
common = []
play = input("Do you want to play? (1 for yes and 0 for no)")
while play == '1':

    for i in range(4):
        num = random.randrange(1,5)
        numbers.append(num)
    for x in range(4):
        guess = int(input("Enter your guesses: "))
        assumptions.append(guess)
    for j in assumptions:
        if j in numbers:
            common.append(j)
    print("These are: ", len(common))
    print("Your gusses are: ", assumptions)
    print("The numbers are", numbers)
    print("You have", len(common), "common numbers with the main list!")
    if len(common) == '4':
        print("You won!")
        common = []
        numbers = []
        assumptions = []
        break
    else:
        play = input("Do you want to play again? (1 for yes and 0 for no)")
        common = []
        numbers = []
        assumptions = []
        if play == '0':
            break