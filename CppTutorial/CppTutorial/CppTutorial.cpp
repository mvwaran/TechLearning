/*

History:
--------------------------------------------------------------------------------------------
1979 - the work that led to C++ started in the fall of 1979 under the name “C with Classes.”
1984 - "C with classes" renamed to C++.
1985 - October 14, First commercial version of C++ released.
1998 - ISO C++
2011 - ISO C++ 11

Highlights:
--------------------------------------------------------------------------------------------
Source c++ files compiled to object files by COMPILER.
Object files are collected as EXE files by LINKER.
The operator << (“put to”) writes its second argument onto its first.       // cout << "Hi";
A declaration is a statement that introduces a name into the program.       // int x;

Operators:
--------------------------------------------------------------------------------------------
Assignment operators    // "="
Arithmetic operators    // +, -,  *, /, %, +x, -x where +x is called unary plus

*/

#include <iostream>

using namespace std;

double square(double x)
{
    return x * x;
}

constexpr double square_constexpr(double x)
{
    return x * x;
}

void print_square(double x)
{
    cout << "Square of " << x << " is " << square(x) << "\n";
}

/*
* CHAPTER 1: MAIN FUNCTION
* 
* If no value is returned, the system will receive a value indicating successful completion.
* A nonzero value from main() indicates failure.
* Not every operating system and execution environment make use of that return value:
* Linux/Unix-based environments often do, but Windows-based environments rarely do.
*/
int main()
{
    print_square(5);

    /*
    * CHAPTER 2: SIZEOF
    * 
    * Byte size of char is 8 bits, but sizeof char will output 1
    * Other datatype size is represented as multiples of char
    */
    cout << "Size of int is " << sizeof(int); // Outputs 4

    /*
    * CHAPTER 3: INITIALIZATION
    */
    int initialization_expl_1 = 7.2;          // i1 becomes 7 (surprise?)
    //int initialization_expl_2 { 7.2 };        // error: floating-point to integer conversion
    //int initialization_expl_3 = { 7.2 };      // error: floating-point to integer conversion (the = is redundant)
    auto initialization_expl_4 = 2;           // similar to javascript var keyword. With auto, we use the = syntax because there is no type conversion involved


    /*
    * CHAPTER 4: Constants
    * 
    * C++ supports two notions of immutability.   // const, constexpr
    * constexpr: meaning roughly “to be evaluated at compile time”. 
    * constexpr is used primarily to specify constants, to allow placement of data in read-only memory (where it is unlikely to be corrupted), and for performance.
    */
    const double const_expl_1 = 17.2;                                   // const_expl_1 is a named constant
    double const_expl_2 = 17.2;                                         // const_expl_2 is not a constant
    constexpr double const_expl_3 = square_constexpr(17.1);             // OK
    //constexpr double const_expl_4 = square_constexpr(const_expl_2);     // error: const_expl_2 is not a constant expression
    const double const_expl_4 = 1.4 * square(const_expl_2);             // OK, may be evaluated at run time
}