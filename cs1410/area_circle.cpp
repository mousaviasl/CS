// This program calculates the area of a circle given its radius.
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    // Declare variables
    double radius;
    cout << "Please enter the radius: ";
    cin >> radius;

    const double pi = 3.1415926535;
    double area;

    // Calculate the area
    area = pow(radius, 2) * pi;

    // Set precision for output
    cout << setprecision(10) << fixed << area << endl;

    return 0;
}