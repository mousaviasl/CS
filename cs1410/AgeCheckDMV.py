print('Welcome to the DMV!')
print("Please use this program to determine if you can apply for a driver's license.")

while True:
    try:
        age = int(input('What is you age?'))
        if age <= 0:
            raise ValueError('Enter a positive number!')
        break
    except TypeError:
        print('Please enter your number in numeric format.')
    except ValueError as err:
        print(err)
        print('You have a Value Error and it is not about if your number is positive or negative.')
    except:
        print('Invalid input')
        
if age < 15:
    print('You cannot apply!')
elif age == 15:
    print("You can apply for a permit and driver's education course.")
elif age >= 16:
    print("You can apply.")