#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    double a;
    double b;
    double c;

    cout << "Please enter the number a: ";
    cin >> a;
    cout << "Please enter the number b: ";
    cin >> b;
    cout << "Please enter the number c: ";
    cin >> c;

    double x_1 = (-b + sqrt(pow(b, 2) - (4 * a * c))) / (2 * a);
    double x_2 = (-b - sqrt(pow(b, 2) - (4 * a * c))) / (2 * a);

    cout << "The first root is: " << x_1 << endl;
    cout << "The second root is: " << x_2 << endl;

    return 0;
}

/*
Input                       Output

a       b       c           x_1         x_2

3       6       -9          1           -3
1       -2      -24         6           -4 
6       3       -6          0.780776    -1.2878
2       4       -8          1.23607     -3.23607
1       4       -20         2.89898     -6.89898
*/