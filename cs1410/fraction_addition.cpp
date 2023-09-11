#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    int a;
    int b;
    char slash;
    cout << "Please enter the first number in the format of a/b: " << endl;
    cin >> a >> slash >> b;

    int c;
    int d;

    cout << "Please enter the second number in the format of c/d: " << endl;
    cin >> c >> slash >> d;
    
    int numenator = (a * d) + (b * c);
    int denominator = b * d;

    cout << numenator << "/" << denominator;

    return 0;
}
