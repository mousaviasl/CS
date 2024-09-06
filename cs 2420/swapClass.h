// swapClass.h
// Author: Esmaeil Mousavi
// Description: Template class definition with three member variables and swap functions

#ifndef SWAPCLASS_H
#define SWAPCLASS_H


template <class myType>
class swapClass {
public:
    void swap12();
    void swap13();
    void swap23();
    myType var1, var2, var3; 

private:
    void swap(myType&, myType&);
};

#include "swapClass.cpp"

#endif