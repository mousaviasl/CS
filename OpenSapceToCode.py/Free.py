import random

numbers = []
assumptions = []
common = []

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