---
title:  "Some Notes on C++ Constructors"
published: true
tags: C++
---

1. The followings are automatically added to every class, if we do not write our own.
    - copy constructor
    - assignment operator
    - a constructor without without any parameter

2. A copy constructor may be called
    - when an object of the class is returned by value
    - when an object of the class is passed (to a function) by value as an argument
    - when an object is constructed based on another object of the same class
    - when compiler generate a temporary object

3. Unlike new, malloc() doesn't call constructor.

4. Object must be passed by reference in copy constructors.

5. We must use initializer list in a constructor when
    - there is a reference variable in class
    - there is a constant variable in class
    - there is an object of another class. And the other class doesn't have default constructor.

6. If a class has a constructor which can be called with a single argument, then this
   constructor becomes conversion constructor because such a constructor allows automatic
   conversion to the class being constructed. A conversion constructor can be called
   anywhere when the type of single argument is assigned to the object.

References: [https://www.geeksforgeeks.org/c-plus-plus-gq/constructors-gq/](https://www.geeksforgeeks.org/c-plus-plus-gq/constructors-gq/)
