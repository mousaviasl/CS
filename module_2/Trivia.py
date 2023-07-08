print("Welcome to my Trivia game!")
print("")
num_correct = 0
num_wrong = 0
correct = ("Congrats! You have chosen the right answer!")
wrong = ("Oops! You are wrong!")
trivia1 = input("What is the name of capital of Japan? ")
if trivia1 == "Tokyo" or trivia1 == "tokyo":
    print(correct)
    num_correct += 1
else:
    print(wrong)
    num_wrong += 1
print("")

trivia2 = float(input("How many Kilometers is a Mile? (Write a decimal number.)"))
if trivia2 == 1.6:
    print(correct)
    num_correct += 1
else:
    print(wrong)
    num_wrong += 1
print("")

trivia3 = int(input("How many minutes is in one day? (Write a number.)"))
if trivia3 == 14400:
    print(correct)
    num_correct += 1
else:
    print(wrong)
    num_wrong += 1
print("")

trivia4 = int(input("How long does it take time to drive from San Diego, CA to Austin, TX (1300 miles distance) if your average speed is 65 mph? (Just write the number of hours.)"))
if trivia4 == 20:
    print(correct)
    num_correct += 1
else:
    print(wrong)
    num_wrong += 1
print("")

trivia5 = input("What langauge Persian people speaking? ")
if trivia5 == "Persian" or trivia5 == "persian" or trivia5 == "Farsi" or trivia5 == "farsi":
    print(correct)
    num_correct += 1
else:
    print(wrong)
    num_wrong += 1
print("")

print(f'You have responded to {num_correct} of the questrions right and {num_wrong} of them wrong! Your total score is % {num_correct/5 * 100 :.2f}!')
if num_correct >= 3:
    print('You have responded to the most of common sense questions right! Congrats!')
else:
    print("You should learn more common sense information!")