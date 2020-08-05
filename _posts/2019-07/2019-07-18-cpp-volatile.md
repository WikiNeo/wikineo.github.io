---
title:  "C++ Volatile Keyword"
published: true
tags: C++
---

## Why do we use volatile keyword?

Consider this code,

```cpp
int some_int = 100;
while(some_int == 100){
    // do something
}
```

When this program gets compiled, the compiler may optimize this code, if it finds that the
program **never** ever makes any attempt to change the value of `some_int`, so it may be
attempted to optimize the `while` loop by changing it from `while(some_int == 100)` to
*something* equivalent to `while(true)` so that the execution could be fast (since the
condition in `while` loop appears to be `true` always). (*if the compiler doesn't optimize
it, then it has to fetch the value of `some_int` and compare it with 100 in each iteration,
which obviously is a little bit slow.*)

However, sometimes, optimization (of some parts of your program) may be **undesirable**,
because it may be that someone else is changing the value of `some_int` from **outside the
program which the compiler is not aware of**, since it can't see it; but it's how you've
designed it. In that case, compiler's optimization would not produce the desired result!

So, to ensure the desired result, you need to somehow stop the compiler from optimizing
the `while` loop. That is where the `volatile` keyword plays its role. All you need to do
is this,

`volatile int some_int = 100;`

Quoting from the C++ standard ($7.1.5.1/8)

> volatile is a hint to the implementation to **avoid aggressive optimization involving
> the object** because the value of the object might be changed by means undetectable by
> an implementation.

References: [https://stackoverflow.com/questions/4437527/why-do-we-use-volatile-keyword](https://stackoverflow.com/questions/4437527/why-do-we-use-volatile-keyword)
