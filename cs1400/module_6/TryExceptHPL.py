
print("""Welcome to the Weber State University Human Performance Lab!
Please utilize the following calculator to find your ideal fat burning heart rate and BMI.
The program will also store this information in a file you choose so that it can be tracked over time.""")

print("Select:")
hpl = 'hBMICalculations.txt'
with open(hpl, 'w') as f:
    data = f.read()
    
1. Create a file
2. Open a file to add results to
3. Read results from file


print("Welcome to the fat burning heart rate and BMI machine!")

while True:
    exception_occurred = False
    
    try:
        age = int(input("Enter the adult's age: "))
        max = 220 - age
        fat_burning = max * 70/100
        weight = int(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        BMI = round((weight / (height**2)), 3)
        
        if age < 0:
            exception_occurred = True
            raise ValueError("Invalid age. Enter a positive number for your age.")
        if max <= 0:
            raise ValueError("Invalid age. You cannot be that old and use this program.")
        if weight < 0:
            exception_occurred = True
            raise ValueError("Invalid weight! Enter a positive number for your weight.")
        if height < 0:
            exception_occurred = True
            raise ValueError("Invalid height! Enter a positive number for your height.")
    except Exception as e:
        print(e)
        exception_occurred = True

    if not exception_occurred:
        break 

f.write("BMI:", BMI)

if BMI < 19:
    f.write("Your BMI is under the normal standard.")
elif BMI <= 25:
    f.write("Your BMI is in the normal range.")
else:
    f.write("Your BMI is over the normal standard.")