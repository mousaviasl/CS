#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int principal_amount;
    double month;
    double rate;

    cout << "Please Enter the amount that you need to take a loan: " << endl;
    cin >> principal_amount;
    cout << "Please enter the number of months that you want to pay the loan back in: " << endl;
    cin >> month;
    cout << "Please enter the interest rate: (i.e., 6.4 %) " << endl;
    cin >> rate;

    if (rate <= 0.0 || month <= 0.0) {
        cout << "Invalid input. Rate and month must be greater than zero." << endl;
        return 1; // Exit with an error code
    }

    double monthly_rate = rate / 12.0 / 100.0;
    double denominator = pow(1.0 + monthly_rate, month) - 1.0;

    if (denominator == 0.0) {
        cout << "Invalid input. Division by zero error." << endl;
        return 1; // Exit with an error code
    }

    double monthly_payment = principal_amount * (monthly_rate * pow(1.0 + monthly_rate, month)) / denominator;

    cout << "The monthly payment is: " << monthly_payment << endl;

    return 0;
}
