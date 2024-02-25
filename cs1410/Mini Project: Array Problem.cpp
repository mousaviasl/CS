#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/* 
Author: Esmaeil Mousavi
Time invested: 17 Min
Description: My program reads five integers, stores them in a vector, 
and calculates the minimum and maximum sums of four out of those five integers
and displays it.
*/

int main() {
    std::vector<int> numbers(5);
    for (int i = 0; i < 5; ++i) {
        cin >> numbers[i];
    }
    
    std::sort(numbers.begin(), numbers.end());

    long long minSum = 0, maxSum = 0;
    for (int i = 0; i < 4; ++i) {
        minSum += numbers[i];
        maxSum += numbers[i + 1];
    }

    cout << minSum << " " << maxSum << endl;
    return 0;
}
