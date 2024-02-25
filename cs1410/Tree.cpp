#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int height;

    cout << "How tall should the tree be?: ";
    cin >> height;

    if (height < 3 || height > 15) {
        cout << "Error: Height must be between 3 and 15." << endl;
        return 1;
    }

    for (int level = 0; level < height; ++level) {

        for (int space = 0; space < height - level - 1; ++space) {
            cout << " ";
        }

        cout << "/";

        for (int space = 0; space < 2 * level; ++space) {
            cout << " ";
        }

        cout << "\\" << endl;
    }

    for (int dash = 0; dash < 2 * height; ++dash) {
        cout << "-";
    }
    cout << endl;

    for (int level = 0; level < height / 2; ++level) {
        for (int space = 0; space < height - 1; ++space) {
            cout << " ";
        }
        cout << "||" << endl;
    }

    return 0;
}
