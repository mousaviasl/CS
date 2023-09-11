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


// Test cases:
/*
1.33            5.5571632448
2.75            23.7582944421
3.25            33.1830724026
4.99            78.2259712314
5.50            95.0331777684
*/