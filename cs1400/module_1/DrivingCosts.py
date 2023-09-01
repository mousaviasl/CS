#inputs: name of three places and their distance from Weber, cost of gas per mile
place1 = input("What is the name of the first area? ")
distance1 = int(input("How many miles " + place1 + " is away from Weber State? "))
place2 = input("What is the name of the second area? ")
distance2 = int(input("How many miles " + place2 + " is away from Weber State? "))
place3 = input("What is the name of the third area? ")
distance3 = int(input("How many miles " + place3 + " is away from Weber State? "))
miles_per_gallon = float(input("How many miles the car can give you ride per each gallon of gas? "))
dollar_per_gallon = float(input("How much is one gallon gas? "))

#calculations
cost1 = (distance1 / miles_per_gallon) * dollar_per_gallon
cost2 = (distance2 / miles_per_gallon) * dollar_per_gallon
cost3 = (distance3 / miles_per_gallon) * dollar_per_gallon

print('')
print('')
print('')
print('')
print('')

#output
print(f'The cost of gas from {place1} to Weber State is {cost1}. \nThe cost of gas from {place2} to Weber State is {cost2}. \nThe cost of gas from {place3} to Weber State is {cost3}. \n ')
