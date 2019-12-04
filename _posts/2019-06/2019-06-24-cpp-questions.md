---
title:  "C++ Questions"
published: true
categories: tech
tags: C++
---

### C++ supports multiple iheritance. What is the "diamond problem" that can occur with multiple inheritance? Give an example

It means that we cannot create hybrid inheritance using multiple and hierachical inheritance.

Let's consider a simple exmaple. A university has people affiated with it. Some are students, some are faculty memebers, some are administrators, and so on. So simple inheritance scheme might have different types of people in different roles, all of whom inherit from one common "Person" class. The Person class could define and abstract `getRole()` method which would then be overriden by its subclass to return the correct role type.

But now what happens if we want to model the role of a Teaching Assistant (TA)? Typically, a TA is both a grad student and a falculty memeber. This yields the classic diamond problem of multiple inheritance and their resulting abiguity regarding the TA's `getRole()` method.

```cpp
class Person {
    public:
        abstract Role getRole();
}

class FalcultyMember : public Person {
    public:
        Role getRole(){
            return Role.Faculty;
        }
}

class GraduateStudent : public Person {
    public:
        Role getRole(){
            return Role.GradStudent;
        }
}

class TA : public FalcultyMember, public GraduateStudent {
}
```

Which `getRole` implementation should the TA inherit? The simple answer might be to have the TA class override the `getRole()` method and return newly-defined `TA`. But that answer is also imperfect as it would hide the fact the a TA is, in fact, both a falculty member and a grad student.

### What is the error in the ccode below and how should it be corrected?

```cpp
my_struct_t *bar;
// ... do stuff, including setting bar to point to a defined my_struct_t object...
memset(bar, 0, sizeof(bar))
```

The last argument to `memset` should be `sizeof(*bar)`, not `sizeof(bar)`. `sizeof(bar)` calculates the size of `bar` (i.e, the pointer itself) rather thant the size of the structure pointed to by `bar`.

A sharp cadidate might point out that using `*bar` will cause a dererenceing error if `bar` has not been assigned. Therefore an even safer solution would be to use `sizeof(my_struct_t)`. However, an even sharper candidate must know that in this case using `*bar` is absolutely safe whithin the call to `sizeof`, even if `bar` has not been initialized yet, since `sizeof` is a compile time construct.

### Assuming buf is a valid pointer, what is the problem in the code below? What would be an alternate way of implementing this that would avoid the problem?

```cpp
size_t sz = buf-size();
while(sz-- >= 0){
    // do something
}
```

The problem ni the above code is that `--sz >= 0` will always be true so you'll never exit the `while` loop.

The reason that `sz-- >= 0` will always be true is that the type of `sz` is `size_t`, which is an alias to one of the fundamental  unsigned integer types. Therefore, since `sz` is unsigned, it can never be less thatn zero.

```cpp
for (size_t i = 0; i < sz; i++){
    // do something
}
```

### Is it possible to have a recursive inline function?

Although you can call an inline function from within itself, the compiler may not generate inline code since the compiler cannot determine the depth of recursion at compile time. A compiler with good optimizer can inline recursive calls till some depth fixed at compile-time (say three or five recursive calls), and insert non-recursive calls at compile time for cases when the actual depth gets execeeded at run time.
