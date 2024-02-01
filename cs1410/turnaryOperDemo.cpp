#include <iostream>
using namespace std;

/*
Ternary operator ?:
Also Called conditional operator

(expl) ? (exp2) : (exp3)

*/

// Write a c++ program to determine if the number entered is ODD or EVEN

int main()
{

    int number;

    cout << "\n Enter the number: ";
    cin >> number;

    // print to the screen if the number is odd or even

    if (number % 2 == 0)
    {
        cout << "The number is EVEN." << endl;
    }

    if (number % 2 == 1)
    {
        cout << "The number is ODD." << endl;
    }

    return 0;
}