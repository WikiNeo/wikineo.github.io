---
title:  "C++ Reference Declaration"
published: true
categories: tech
tags: C++
---

Declares a named vairable as a reference, that is, an alias to an already-existing object or function.

## Syntax

A reference vairable declaration is any simple declaration whose declarator has the form

- & attr(optional) declarator => lvalue reference declarator: the declaration `S& D;` declares D as an lvalue reference to the type determined by decl-specifier-seq S.
- && attr(optional) declarator (since C++11) => rvalue reference declaration: the declaration `S&& D;` declares D as an rvalue reference to the type determined by decl-specifier-seq S.
- declarator - any declarator except another reference declarator (there are no references to references)
- attr(C++11) - optional list of attributes

A reference is rquired to be initalized to refer to a valid object or function.

There are no reference to void and to reference to reference.

Reference types cannot be cv-qualified at the top level; there is no syntax for that declration, and if a qualification is introduced
through a typedef, decltype, or template type argument, it is ignored.

References are not objects; they do not necessarily occupy storage, although the compiler may allocate storge if it is necessary to 
implement the descired sematics (e.g. a non-static data member of reference type usually increases the size of the class by the amount
necessary to storea memroy address).

Because references are not objects, there are no arrays of references, no pointers to reference, and no references to references:

```cpp
int& a[3];  // error, no array of reference
int& *p;    // error, no pointer to referencce
int& &r;    // error, no reference to reference
```

### Reference collapsing

It is permitted to form references to references through type manipulation in templates or typedefs, in which case the reference 
collapsing rules apply: rvalue reference to rvalue reference collpases to rvalue reference, all other combinations form lvelu reference:

```cpp
typedef int& lref;
typedef int&& rref;
int n;

lref&  r1 = n;   // type of r1 is int&
lref&& r2 = n;   // type of r2 is int&
rref&  r3 = n;   // type of r3 is int&
rref&& r4 = n;   // type of r4 is int&&
```

(This, along with special rules for template argument deduction when T&& is used in a function template, forms the rules that make
std::forward possible.)

## Lvalue references

Lvalue references can be used to alias an existing object (optionally with different cv-qualification):

```cpp
#include <iostream>
#include <string>

int main(){
    std::string s = "Ex";
    std::string& r1 = s;
    const std::string& r2 = s;

    r1 += "ample";              // modifies s
    //r2 += "!";                // error: cannot modify through reference to const
    std::cout << r2 << '\n';    // print s, which now holds "Example"
}
```

They can also be used to implement pass-by-reference semantics in function calls:

```cpp
#include <iostream>
#include <string>

void double_string(std::string& s){
    s += s; // s is the same object as main()'s str
}

int main(){
    std::string str = "Test";
    double_string(str);
    std::cout << str << '\n';   \\ TestTest
}
```

When a function's return type is lvalue reference, the function call expression becomes an lvalue expression:

```cpp
#include <iostream>
#include <string>

char& char_number(std::string& s, std::size_t n){
    return s.at(n); // string::at() returns a reference to char
}

int main(){
    std::string str = "Test";
    char_number(str, 1) = 'a';  // the function call is lvalue, can be assigned to
    std::cout << str << '\n';   // Tast
}
```

## Rvalue references

Rvalue references can be used to extend the lifetimes of temporary objects

```cpp
#include <iostream>
#include <string>

int main(){
    std::string s1 = "Test";
    //std::string&& r1 = s1;  // error cannot bind to lvalue

    const std::string& r2 = s1 + s1;    // okay: lvalue reference to const extends lifetime
    //r2 += "Test";   // error: cannot modify through reference to const

    std::string&& r3 = s1 + s1; // okay: rvalue reference extends lifetime
    r3 += "Test";   // okay: can modify through reference to non-const
    std::cout << r3 << '\n\;    // TestTestTest
}
```

More importantly, when a function has both rvalue referene and lvalue reference overloads, the rvalue reference overload binds
binds to rvalues, while the lvalue reference overload binds to lvalues

```cpp
#include <iostream>
#include <utility>
 
void f(int& x) {
    std::cout << "lvalue reference overload f(" << x << ")\n";
}
 
void f(const int& x) {
    std::cout << "lvalue reference to const overload f(" << x << ")\n";
}
 
void f(int&& x) {
    std::cout << "rvalue reference overload f(" << x << ")\n";
}
 
int main() {
    int i = 1;
    const int ci = 2;
    f(i);  // calls f(int&)
    f(ci); // calls f(const int&)
    f(3);  // calls f(int&&)
           // would call f(const int&) if f(int&&) overload wasn't provided
    f(std::move(i)); // calls f(int&&)
 
    // rvalue reference variables are lvalues when used in expressions
    int&& x = 1;
    f(x);            // calls f(int& x)
    f(std::move(x)); // calls f(int&& x)
}
```

Because rvalue references can bind to xvalues, they can refer to non-temporary objects:

```cpp
int i2 = 42;
int&& rri = std::move(i2);  // binds directly to i2
```

This makes it possible to move out of an object in scope that is no longer needed:

```cpp
std::vector<int> v{1, 2, 3, 4, 5};
std::vector<int> v2(std::move(v));  // binds an rvalue reference to v
assert(v.empty());
```
