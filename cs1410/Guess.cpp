#include <iostream>
#include <random>
#include <chrono>
using namespace std;

int main()
{

    default_random_engine rng((unsigned)(chrono::system_clock::now().time_since_epoch().count()));
    uniform_int_distribution<int> range(1, 100);
    

    int target = range(rng);
    int guess;

    do {

        cout << "Please guess a number between 1 and 100: ";
        cin >> guess;


        if (guess == 0) break;


        if (guess == target) {
            cout << "You win!" << endl;
            break;
        } 

        else if (guess < target) {
            cout << "You have guessed low, try again..." << endl;
        } 

        else {
            cout << "You have guessed high, try again..." << endl;
        }
    } while (guess != target);

    return 0;
}
