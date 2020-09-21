---
title: "Double ampersand (&&) in C++11"
published: true
tags: C++
---

The biggest difference between a C++03 reference (now called an lvalue reference
in C++11) is that it can bind to an rvalue like a temporary without having to be
const. Thus, this syntax is now legal

```
T&& r = T();
```

rvalue references primarily provide for the following

## Move semantics

A move constructor and move assignment operator can now be defined that takes an
rvalue reference instead of the usual const-lvalue reference. A move functions
like a copy, except it is not obliged to keep the source unchanged; in fact, it
usually modifies the source such that it no longer owns the owned resources.
This is great for eliminating extraneous copies, especially in standard library
implementations.

For example, a copy constructor might look like this

```cpp
foo(foo const& other)
{
    this->length = other.length;
    this->ptr = new int[other.length];
    copy(other.ptr, other.ptr + other.length, this->ptr);
}
```

If this constructor was passed a temporary, the copy would be unnecessary
because we know the temporary will just be destroyed; why not make use of the
resources the temporary already allocated? In C++03, there's no way to prevent
the copy as we cannot determine we were passed a temporary. In C++11, we can
overload a move constructor

```cpp
foo(foo&& other)
{
   this->length = other.length;
   this->ptr = other.ptr;
   other.length = 0;
   other.ptr = nullptr;
}
```

Notice the big difference here: the move constructor actually modifies its
argument. This would effectively "move" the temporary into the object being
constructed, thereby eliminating the unnecessary copy.

The move constructor would be used for temporaries and for non-const lvalue
references that are explicitly converted to rvalue references using the
`std::move` function (it just performs the conversion). The following code both
invoke the move constructor for `f1` and `f2`

```cpp
foo f1((foo())); // Move a temporary into f1; temporary becomes "empty"
foo f2 = std::move(f1); // Move f1 into f2; f1 is now "empty"
```

## Perfect forwarding

rvalue references allow us to properly forward arguments for templated
functions. Take for example this factory function:

```cpp
template <typename T, typename A1>
std::unique_ptr<T> factory(A1& a1)
{
    return std::unique_ptr<T>(new T(a1));
}
```

If we called `factory<foo>(5)`, the argument will be deduced to be `int&`, which
will not bind to a literal 5, even if `foo`'s constructor takes an `int`. Well,
we could instead use `A1 const&`, but what if `foo` takes the constructor
argument by non-const reference? To make a truly generic factory function, we
could have to overload factory on `A1&` and on `A1 const &`. That might be fine
if factory takes 1 parameter type, but each additional parameter type would
multiply the necessary overload set by 2. That's very quickly unmaintainable.

rvalue references fix this problem by allowing the standard library to define a
`std::forward` function that can properly forward lvalue/rvalue references.

This enables us to define the factory function like this

```cpp
template <typename T, typename A1>
std::unique_ptr<T> factory(A1&& a1)
{
    return std::unique_ptr<T>(new T(std::forward<A1>(a1)));
}
```

Now the argument's rvalue/lvaue-ness is preserved when passed to `T`'s
constructor. That means the if factory is called with an rvalue, `T`'s
constructor is called with an rvalue. If factory is called with an lvalue, `T`'s
constructor is called with an lvalue. This improved function works because of
one special rule

> when the function parameter type is of the form `T&&` where `T` is a template
> parameter, and the function argument is an lvalue of type `A`, the type `A&`
> is used for template argument deduction.

Thus, we can use factory like so

```cpp
auto p1 = factory<foo>(foo()); // calls foo(foo&&)
auto p2 = factory<foo>(*p1);   // calls foo(foo const&)
```

## Important rvalue reference properties

- For overload resolution, lvalues prefer binding to lvalue reference and rvalues
  prefer binding to rvalue references. Hence why temporaries prefer invoking a
  move constructor/move assignment operator over a copy constructor/assignment
  operator.

- rvalue references will implicitly bind to rvalues and to temporaries that are
  the result of an implicit conversion. i.e. `float f = 0f; int&& i = f;` is
  well formed because float is implicitly convertible to int; the reference
  would be to a temporary that is the result of the conversion.

- Named rvalue reference are lvalues. Unnamed rvalue references are rvalues.
  This is important to understand why the `std::move` call is necessary in: `foo&& r = foo(); foo f = std::move(r);`

## Reference

- [https://stackoverflow.com/questions/5481539/what-does-t-double-ampersand-mean-in-c11](https://stackoverflow.com/questions/5481539/what-does-t-double-ampersand-mean-in-c11)