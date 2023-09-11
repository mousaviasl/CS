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

/*
Test Cases:

Fraction1       Fraction2       Sum
1/3             2/5             11/15
1/4             2/3             11/12  
1/2             1/2             4/4
7/10            9/15            195/150
76/80           95/100          15200/80000
*/
