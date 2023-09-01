power = input("Do you want to start? (y/n)")
num = int(input("Enter a number and we will show its factors for you: "))
factor = []
while power != 'n':
  factor = []
  for i in range (1, num + 1):
    if num % i == 0:
      factor.append(i)
  print(factor)
  power = input("Do you want to continue? (y/n)")
  if power != 'n':
    num = int(input("Enter a number and we will show its factors for you: "))
  else:
    print("Done!")
    break