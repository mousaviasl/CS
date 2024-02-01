// I have added all the important lecture nnotes in the form of comment to my code here and also exaplinedw what I have done.
#include <iostream>

// Using the standard namespace to avoid writing `std::` before every standard function
using namespace std;

// Definition of a struct named 'Cars' to represent car attributes
struct Cars {
    string brand;  // To store the brand of the car
    string model;  // To store the model name of the car
    double price;  // To store the price of the car
    int year;      // To store the manufacturing year of the car
};

// Forward declaration of the 'printCar' function
void printCar(Cars car);

// Main function: Entry point of the program
int main() {
    // Initializing five car objects with their respective details
    Cars car1 = { "Mercedes", "C Class", 80000.0, 2023 };
    Cars car2 = { "Mclaren", "P1", 800000.0, 2015 };
    Cars car3 = { "Mazda", "6", 15000.0, 2020 };
    Cars car4 = { "Maserati", "Ghibli", 45000.0, 2016 };
    Cars car5 = { "Mitsubishi", "Lancer", 10000.0, 2013 };

    // Calling the 'printCar' function to print the details of 'car1'
    printCar(car1);
}

// Function definition of 'printCar'
void printCar(Cars car) {
    // Printing the brand of the car
    cout << "Brand: " << car.brand << endl;
    
    // Printing the model name of the car
    cout << "Model: " << car.model << endl;
    
    // Printing the price of the car with a dollar sign for representation
    cout << "Price: $" << car.price << endl;
    
    // Printing the manufacturing year of the car
    cout << "Year: " << car.year << endl;
}
