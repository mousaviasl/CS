import math
print("Quadradic formula")
print()
print()
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))
print()
print()
print()
x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print()
print()
print()
print(f'The solutions are {x1:.2f} and {x2:.2f}')
print()
print()