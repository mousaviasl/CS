while True:
    try:
        age = int(input('What is your age?'))
        break
    except ValueError:
        print('Please enter a valid number.')