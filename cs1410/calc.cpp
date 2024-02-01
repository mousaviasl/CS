#include <iostream>
using namespace std;

int main() {
    char inChoice = 'x';
    
    int num1;
    int num2;
    
    int result;
    
    cout << "Please enter number 1: ";
    cin >> num1;
    cout << "Please enter number 2: ";
    cin >> num2;
    cout<< endl;
    
    cout << "Please enter your choice of math: " << endl;
    cout << "a for addition" << endl;
    cout << "s for subtraction" << endl;
    cout << "m for multiplicarion" << endl;
    cout << "d for division" << endl;
    cout << "Please enter math choice: " << endl;
    cin >> inChoice;
    
    switch (inChoice) {
        case 'a':
        case 'A':
        case '+':
        result = num1 + num2;
        break;
        
        case 's':
        case 'S':
        case '-':
        result = num1 - num2;
        break;
        
        case 'm':
        case 'M':
        case '*':
        result = num1 * num2;
        break;
        
        case 'd':
        case 'D':
        case '/':
        result = num1 / num2;
        break;
        
        default:
        cout << "Not a valid choice" << endl;
        result = 99999;
        break;
    }
    
    cout << "Your result is: " << result << endl;
    
    return 0;
}