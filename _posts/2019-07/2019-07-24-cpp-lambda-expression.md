---
title:  "C++ Lambda Expression"
published: true
categories: tech
tags: C++
---

C++11 introduces lambadas allow you to write inline, anonymous functor.

```cpp
void func3(vector<int>& v){
    for_each(v.begin() v.end(), [](int){
        // do something
    })
}
```

Lambda functions are just syntactic sugar for anonymous functors.

## Return Types

In simple cases the return type of the lambda is deduced for you,

```cpp
void func4(vector<double>& v){
    transform(v.begin(), v.end(), v.begin()), [](double){
        return d < 0.000001 ? 0 : d;
    }
}
```

To explicitly specify a return type, using `-> T`

```cpp
void func4(vector<double>& v){
    transform(v.begin(), v.end(), v.begin(), [](double d) -> double {
        return d < 0.001 ? 0 : d;
    })
}
```

## Capturing variables

```cpp
void func5(vector<double>& v, const double& epsilon){
    transform(v.begin(), v.end(), v.begin(), [epsilon](double d) -> double {
        return d < epsilon ? 0 : d;
    })
}
```

- `[&epsilon]` capture by reference
- `[&]` captures all variables used in the lambda by reference
- `[=]` captures all variables used in the lambda by value
- `[&, epsilon]` captures variables like with [&], but epsilon by value
- `[=, &epsilon]` captures variables like with [&], but epsilon by reference

References: [https://stackoverflow.com/questions/7627098/what-is-a-lambda-expression-in-c11](https://stackoverflow.com/questions/7627098/what-is-a-lambda-expression-in-c11)
