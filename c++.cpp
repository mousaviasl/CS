#include <iostream>
using namespace std;

int main() {
    int num = 7;
    if (num > 0 && num < 5) {
        cout << "First" << endl;
    }
    else if (num > 0 || num < 5) {
        cout << "Second" << endl;
    }
    else {
        cout << "Third" << endl;
    }
    return 0;
}