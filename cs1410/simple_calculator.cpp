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
    cout << "Please enter the interest rate: (i.e. 6.4 %) " << endl;
    cin >> rate;
    rate = rate / 100.0;
    double monthly_payment = principal_amount * (((rate / 12) * (pow((1 + (rate / 12)), month))) / ((pow((1 + (rate / 12)), month)) -1));
    cout << "The monthly payment is: " << fixed << monthly_payment << endl;
    

    return 0;

}