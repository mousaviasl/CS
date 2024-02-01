#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (1 <= n && n <= 9) {
        string numbers[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        cout << numbers[n - 1] << endl;
    } else {
        cout << "Greater than 9" << std::endl;
    }
    return 0;
}
