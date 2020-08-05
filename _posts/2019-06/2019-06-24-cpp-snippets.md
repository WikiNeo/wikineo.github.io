---
title:  "C++ Snippets"
published: true
tags: C++
---

### Performance

#### Unary Operator

```cpp
vector vec;
for(auto itr = vec.begin(); itr != vec.end(); itr++){
    itr.print();
}
```

```cpp
vector vec;
for(auto itr = vec.begin(); itr != vec.end(); ++itr){
    itr.print();
}
```

The second is better from a performance standpoint. This is because the post-increment operator is more expensive than the pre-increment operator. The underlying implementation of the post-increment oprator makes a copy of the element before incrementing it and then returns the copy.

That said. many compilers will automatically optimize the first option by converting it into the second.

### Inheritance

```cpp
#include <iostream>

class Base {
    virtual void method() {std::cout << "from Base" << std::endl;}
public:
    virtual ~Base() {method();}
    void baseMethod() {method();}
};

class A : public Base {
    void method() {std::cout << "from A" << std::endl;}
public:
    ~A() {method();}
};

// from A
// from A
// from Base
int main(void) {
    Base* base = new A;
    base->baseMethod();
    delete base;
    return 0;
}
```

### Exception

#### Exception in Exception

```cpp
#include <iostream>

class A {
    public:
        A() {}
        ~A(){
            throw 42;
        }
};

// This program will terminate abnormally. `throw 32` will start unwinding the stack and destroy class A. The class A destructor will 
// throw another excception during the exception handling, which will cause program to crash.
int main(int argc, const char *argv[]){
    try {
        A a;
        throw 32;
    } catch (int a){
        std::cout << a;
    }
}
```

### Array and Pointer

#### Pointer Operation

```cpp
#include <iostream>

// 8 -> a[4] - a[0] + a[3]
int main(int argc, const char *argv[]){
    int a[] = {1, 2, 3, 4, 5, 6};
    std::cout << (1 + 3)[a] - a[0] + (a + 1)[2];
}
```

### Basics

#### Unary Operators

```cpp
int i = 5;
int j = i++;

// i == 6, j == 5
```

#### Variable Type

```cpp
#include <iostream>

// 2^32 - 25
int main(int argc, char **argv)
{
    std::cout << 25u - 50;
    return 0;
}
```

```cpp
unsigned char half_limit = 150;

// this is an infinite loop
for (unsigned char i = 0; i < 2 * half_limit; ++i)
{
    // do something;
}
```
