#include <iostream>
using namespace std;


int main()
{

    int number1;
    int number2;
    int maxNum;

    cout << "\n Enter the number 1: ";
    cin >> number1;

    cout << "\n Enter the number 2: ";
    cin >> number2;

    /*
    if (number1 > number2)
    {
        cout << "The number 1 is greater than number 2." << endl;
    }
    */

   maxNum = (number1 > number2) ? number1 : number2;
   cout << "\n The maximum is: " << maxNum << endl;


    return 0;
}