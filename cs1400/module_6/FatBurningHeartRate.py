print("Welcome to the fat burning heart rate and BMI machine!")

try:
    age = int(input("Enter the adult's age: "))
    max = 220 - age
    fat_burning = max * 70/100
    weight = int(input("Enter your weight in Kilograms: "))
    height = int(input("Enter your height in meters: : "))
    BMI = weight / (height**2)
    
    if age < 18:
        raise ValueError("You are so young and our machine cannot calculate your fat-burning heart rate.")
except 
print(BMI)
if BMI < 19:
    print("You BMI is under the normal standard.")
elif BMI <= 25:
    print("Your BMI is in the normal range.")
else:
    print("Your BMI is over the normal standard.")