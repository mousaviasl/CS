class PositiveNumberForAgeError(Exception):
    pass

class SoOldPersonError(Exception):
    pass

class PositiveNumberForWeightError(Exception):
    pass

class PositiveNumberForHeightError(Exception):
    pass

print("""Welcome to the Weber State University Human Performance Lab!
Please utilize the following calculator to find your ideal fat burning heart rate and BMI.
The program will also store this information in a file you choose so that it can be tracked over time.""")

hpl_filename = 'hBMICalculations.txt'

try:
    with open(hpl_filename, 'w') as f:
        print("Welcome to the fat burning heart rate and BMI machine!")

        while True:
            exception_occurred = False

            try:
                age = int(input("Enter the adult's age: "))
                max_heart_rate = 220 - age
                fat_burning = max_heart_rate * 70/100
                weight = int(input("Enter your weight in kilograms: "))
                height = float(input("Enter your height in meters: "))
                BMI = round((weight / (height**2)), 3)

                if age < 0:
                    raise PositiveNumberForAgeError("Invalid age. Enter a positive number for your age.")
                if max_heart_rate <= 0:
                    raise SoOldPersonError("Invalid age. You cannot be that old and use this program.")
                if weight < 0:
                    raise PositiveNumberForWeightError("Invalid weight! Enter a positive number for your weight.")
                if height < 0:
                    raise PositiveNumberForHeightError("Invalid height! Enter a positive number for your height.")

            except PositiveNumberForAgeError as psa:
                print(psa)
                exception_occurred = True
            except SoOldPersonError as soe:
                print(soe)
                exception_occurred = True
            except PositiveNumberForWeightError as pnw:
                print(pnw)
                exception_occurred = True
            except PositiveNumberForHeightError as pnh:
                print(pnh)
                exception_occurred = True

            if not exception_occurred:
                break

        f.write("Age: {}\n".format(age))
        f.write("Max Heart Rate: {}\n".format(max_heart_rate))
        f.write("Fat Burning Heart Rate: {}\n".format(fat_burning))
        f.write("Weight: {} kg\n".format(weight))
        f.write("Height: {} meters\n".format(height))
        f.write("BMI: {}\n".format(BMI))

        if BMI < 19:
            f.write("Your BMI is under the normal standard.\n")
        elif BMI <= 25:
            f.write("Your BMI is in the normal range.\n")
        else:
            f.write("Your BMI is over the normal standard.\n")

except Exception as e:
    print("An error occurred:", e)


try:
    with open(hpl_filename, 'r') as f:
        contents = f.read()
        print("\nFile Contents:")
        print(contents)
except FileNotFoundError:
    print("File not found.")