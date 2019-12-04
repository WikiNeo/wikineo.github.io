---
title:  "C++ Virtual Functions"
published: true
categories: tech
tags: C++
---

## Why do we need virtual functions in C++?

Let's say you have these two classes:

```cpp
class Animal {
    public:
        void eat(){ 
            cout << "I am eating generic food.";
        }
};

class Cat : public Animal {
    public:
        void eat(){
            cout << "I am eating a rat.";
        }
}
```

In your main function:

```cpp
Animal* animal = new Animal;
Cat* cat = new Cat;

animal->eat();  // I'm eating generic food
cat->eat();     // I'm eating a rat
```

Let's change it a little now so that `eat()` is called via an intermediate function

```cpp
void func(Animal *xyz) {
    xyz->eat();
}
```

Now our main function is:

```cpp
Animal* animal = new Animal;
Cat* cat = new Cat;

func(animal);   // I'm eating generic food
func(cat);      // I'm eating generic food
```

The solution is to make `eat()` from the `Animal` class a virtual function.

references: [https://stackoverflow.com/questions/2391679/why-do-we-need-virtual-functions-in-c](https://stackoverflow.com/questions/2391679/why-do-we-need-virtual-functions-in-c)
