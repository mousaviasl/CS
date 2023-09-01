# Tip Calcualtor
# Input the cost of food

total = 0
percentage = 0
food = float(input("How much was the cost of your food? "))
service = input("How would your rate your service? Use Excellent, Good or Poor to rate your experince.")
percentage += 0.10
if service == "Excellent" or service == "excellent":
    percentage += 0.10
elif service == "Good" or service == "good":
    percentage += 0.05
elif service == "Poor" or service == "poor":
    total = (percentage + 1) * food
else:
    print(f'{service} is an invalid word to rate your experience. Please use Excellent, Good or Poor to rate your experince.')

#calcuations

total = (percentage + 1) * food

#Output
print('The total cost is: ', round(total, 2))