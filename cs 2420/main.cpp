// main.cpp
// Author: Esmaeil Mousavi
// Description: Test program to instantiate swapClass with test the swap methods.

#include <iostream>
#include "swapClass.h"

int main() {

    swapClass<int> swapInts;
    swapInts.var1 = 1;
    swapInts.var2 = 2;
    swapInts.var3 = 3;

    std::cout << "Before swapping (integers): " << swapInts.var1 << ", " << swapInts.var2 << ", " << swapInts.var3 << std::endl;
    
    swapInts.swap12();
    std::cout << "After swapping var1 and var2: " << swapInts.var1 << ", " << swapInts.var2 << ", " << swapInts.var3 << std::endl;

    swapInts.swap13();
    std::cout << "After swapping var1 and var3: " << swapInts.var1 << ", " << swapInts.var2 << ", " << swapInts.var3 << std::endl;

    swapInts.swap23();
    std::cout << "After swapping var2 and var3: " << swapInts.var1 << ", " << swapInts.var2 << ", " << swapInts.var3 << std::endl;

    swapClass<std::string> swapStrings;
    swapStrings.var1 = "one";
    swapStrings.var2 = "two";
    swapStrings.var3 = "three";

    std::cout << "\nBefore swapping (strings): " << swapStrings.var1 << ", " << swapStrings.var2 << ", " << swapStrings.var3 << std::endl;
    
    swapStrings.swap12();
    std::cout << "After swapping var1 and var2: " << swapStrings.var1 << ", " << swapStrings.var2 << ", " << swapStrings.var3 << std::endl;

    swapStrings.swap13();
    std::cout << "After swapping var1 and var3: " << swapStrings.var1 << ", " << swapStrings.var2 << ", " << swapStrings.var3 << std::endl;

    swapStrings.swap23();
    std::cout << "After swapping var2 and var3: " << swapStrings.var1 << ", " << swapStrings.var2 << ", " << swapStrings.var3 << std::endl;

    return 0;
}