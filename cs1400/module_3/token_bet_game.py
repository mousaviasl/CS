import random
print()
print()
print("Esmaeil's Slot Machine")
print()
print()
tokens = int(input("Enter the starting number of tokens you wish to use: "))
print()
print()
iteration = 0 
num_tokens = int(input("How much you token/tokens want to bet? (Press -1 to quit.)"))
print()
print()
while iteration < 2:
    if num_tokens == -1:
        break
    num1 = random.randrange(1,6)
    num2 = random.randrange(1,6)
    num3 = random.randrange(1,6)
    if num1 == num2 == num3:
            print(f'You won {num1 + num2 + num3} tokens!')
            tokens = num1 + num2 + num3 + tokens
            print(f'Total tokens after your win: {tokens}')
    else:
        print(f'You lost {num_tokens} tokens. :(')
        tokens = tokens - num_tokens
        print(f'Total left tokens: {tokens}')
        
    iteration = iteration + 1
    num_tokens = int(input("How much you token/tokens want to bet? (Press -1 to cash out.)"))

print()
print()
print(f'Total tokens that you made: {tokens}')
print("Thanks for playing!")