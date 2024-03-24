"""Date: 02/29/2024
Program Name: Customer Discount
Time Invested: 12 minutes
Author: Esmaeil Mousavi"""

def calculate_discount(amount):
    if amount >= 500:
        discount_rate = 0.4
    elif amount >= 200:
        discount_rate = 0.2
    else:
        discount_rate = 0.1
    return amount * discount_rate
def main():
    amount = float(input("Enter the amount of merchandise: "))
    discount = calculate_discount(amount)
    amount_payable = amount - discount
    print("\nCalculating the discount......\n")
    print("******Amount payable is: {:.2f}".format(amount_payable))
if __name__ == "__main__":
    main()
