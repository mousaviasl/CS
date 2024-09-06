// swapClass.cpp
// Author: Esmaeil Mousavi
// Description: Template class - swapClass functions

// Swap var1 and var2
template <class myType>
void swapClass<myType>::swap12() {
    swap(var1, var2);
}

template <class myType>
void swapClass<myType>::swap13() {
    swap(var1, var3);
}

template <class myType>
void swapClass<myType>::swap23() {
    swap(var2, var3);
}

template <class myType>
void swapClass<myType>::swap(myType& first, myType& second) {
    myType temp = first;
    first = second;
    second = temp;
}