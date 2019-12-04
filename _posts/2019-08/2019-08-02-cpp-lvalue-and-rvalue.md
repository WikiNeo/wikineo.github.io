---
title:  "Understanding the meaning of lvalues and rvalues in C++"
published: true
categories: tech
tags: C++
---

## Lvalues and rvalues: a friendly definition

In C++ an *lvalue* is something that points to a specific memory location.

A *rvalue* is something that doesn't point to anywhere.

In general, rvalues are temporary and short lived, while lvalues live a longer life since
they exist as variables. It's also fun to think of lvalues as *containers* and rvalue as
*things contained in the container*.

```cpp
int x = 666;
```

Here `666` is an rvalue; a number (technically a *literal constant*) has no specific
memory address, except for some temporary register while the program is running. That
number is assigned to `x`, which is a variable. A variable has a specific memory location,
so its an lvalue. C++ states that an assignment requires an lvalue as its left operand:
this is perfectly legal;.

```cpp
int* y = &x;
```

Here I'm grabbing the memory address of `x` and putting it into `y`, through the
address-of operator `&`. It takes an lvalue argument and produces an rvalue. This is
another perfectly legal operation: on the left side of the assignment we have an lvalue (a
variable), on the right side an rvalue produced by the address-of operator.

```cpp
int y;
666 = y; //error!
```

The technical reason is that `666`, being a literal constant - so an rvalue, doesn't have
a specific memory location. `y` is assigned nowhere.

```cpp
int* y = &666; // error
```

The `&` operator wants an lvalue in input, because only an lvalue has an address that `&`
can process.

## Functions returning lvalues and rvalues

Left operand of an assignment must be an lvalue.

```cpp
int setValue(){
    return 6;
}

setValue() = 3; // error
```

`setValue()` returns an rvalue (the temporary number `6`), which cannot be a left operand
of assignment. 

```cpp
int global = 100;

int& setGlobal(){
    return global;
}

setGlobal = 400;    // ok
```

It works because `setGlobal` returns a reference.

## Lvalue to rvalue conversion

An lvalue  may get converted to an rvalue. According to the C++ specification, it takes
two rvalues as arguments and return an rvalue.

```cpp
int x = 1;
int y = 3;
int z = x + y;
```

`x` and `y` have undergone an implicit **lvalue-to-rvalue conversion**

## Lvalue references

```cpp
int y = 10
int& yref = y;
yref++;         // y is now 11
```

`yref` is of type `int&`: a reference to `y`. It's called an **lvalue reference**

```cpp
void fnc(int& x){

}

int main(){
    fuc(10);    // error
    int x = 10;
    fnc(x);     // ok
}
```

## Const lvalue reference to the rescue

*You are allowed to bind a const lvalue to an rvalue*

```cpp
// this
const int& ref = 10;    // OK!

// would translate to
int __internal_unique_name = 10;
const int& ref = __internal_unique_name;

void fnc(const int& x){

}

int main(){
    fnc(10);    // ok
}
```

References: [https://www.internalpointers.com/post/understanding-meaning-lvalues-and-rvalues-c](https://www.internalpointers.com/post/understanding-meaning-lvalues-and-rvalues-c)


























