/* Date: 01/16/2024
Program Name: Cones
Time Invested: 20 minutes
Author: Esmaeil Mousavi*/

#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
using namespace std;

    int main() {
    double V, S, r, h;
    cout << "Enter the radius and height of the cone: ";
    cin >> r >> h;
    V = (M_PI * r * r * h) * (3.0);
    cout << "Volume of the cone: " << V << endl;
    S = M_PI * r * (r + sqrt(h * h + r * r));
    cout << "Surface area of the cone: " << S << endl;
    return 0;
}