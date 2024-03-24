/* Date: 02/29/2024
Program Name: Roots
Time Invested: 18 minutes
Author: Esmaeil Mousavi*/

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double a, b, c, x1, x2, discriminant;
    cout << "Enter a, b and c: ";
    cin >> a >> b >> c;
    discriminant = b * b - 4 * a * c;
    x1 = (-b + sqrt(discriminant)) / (2 * a);
    x2 = (-b - sqrt(discriminant)) / (2 * a);
    cout << "-------- Roots ---------" << endl;
    cout << "x1 = " << x1 << endl;
    cout << "x2 = " << x2 << endl;
    return 0;
}