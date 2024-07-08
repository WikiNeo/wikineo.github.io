---
title:  "C++ Rvalue References"
published: true
tags: C++
---

### Definition of lvalue and rvalue

- An *lvalue* is an expression that refers to a memory location and allows us to take the address of that
memory location via the & operation.

- An *rvalue* is an expression that is not an lvalue.

```cpp
  // lvalues:
  //
  int i = 42;
  i = 43; // ok, i is an lvalue
  int* p = &i; // ok, i is an lvalue
  int& foo();
  foo() = 42; // ok, foo() is an lvalue
  int* p1 = &foo(); // ok, foo() is an lvalue

  // rvalues:
  //
  int foobar();
  int j = 0;
  j = foobar(); // ok, foobar() is an rvalue
  int* p2 = &foobar(); // error, cannot take the address of an rvalue
  j = 42; // ok, 42 is an rvalue

```

### Move Semantics

Suppose X is a class that holds a pointer to some resource,say, m_pResource.

The copy assignment operator for X:

```cpp
X& X::operator=(X const & rhs)
{
  // [...]
  // Make a clone of what rhs.m_pResource refers to.
  // Destruct the resource that m_pResource refers to. 
  // Attach the clone to m_pResource.
  // [...]
}
```

Use x as follows

```cpp
X foo();
X x;
x = foo();
```

The last line above

- clones the resource from the temporary return by foo,
- destructs the resource held by x and replaces it with the clone,
- destructs the temporary and thereby releases its resource.

Rather obviously, it would be ok, and much more efficient, to swap resource pointers (handles) between x and 
the temporary, and then let the temporary's destructor destruct x's original resource. In other words, in the 
special case where the right hand side of the assignment is an rvalue, we want the copy assignment operator 
to act like this:

```cpp
X& X::operator=(<mystery type> rhs)
{
  // [...]
  // swap this->m_pResource and rhs.m_pResource
  // [...]  
}
```

This is called *move semantics*.

### Rvalue references


If X is any type, then X&& is called an rvalue reference to X. For better distinction, the ordinary 
reference X& is now also called an lvalue reference.

An rvalue reference is a type that behaves much like the ordinary reference X&, with several exceptions. 
The most important one is that when it comes to function overload resolution, lvalues prefer old-style lvalue 
references, whereas rvalues prefer the new rvalue references:

```cpp
void foo(X& x); // lvalue reference overload
void foo(X&& x); // rvalue reference overload

X x;
X foobar();

foo(x); // argument is lvalue: calls foo(X&)
foo(foobar()); // argument is rvalue: calls foo(X&&)

```

> Rvalue references allow a function to branch at compile time (via overload resolution) on the condition 
> "Am I being called on an lvalue or an rvalue?"

### Forcing Move Semantics

Using std::move wherever we can, as shown in the swap function above, gives us the following important benefits:

- For those types that implement move semantics, many standard algorithms and operations will use move 
semantics and thus experience a potentially significant performance gain. An important example is inplace '
sorting: inplace sorting algorithms do hardly anything else but swap elements, and this swapping will now 
take advantage of move semantics for all types that provide it.

- The STL often requires copyability of certain types, e.g., types that can be used as container elements. 
Upon close inspection, it turns out that in many cases, moveability is enough. Therefore, we can now use 
types that are moveable but not copyable (unique_pointer comes to mind) in many places where previously, 
they were not allowed. For example, these types can now be used as STL container elements.

Consider a simple assignment between variables, like this:

```cpp
a = b;
```

What do you expect to happen here? You expect the object held by a to be replaced by a copy of b, and in 
the course of this replacement, you expect the object formerly held by a to be destructed. Now consider the line

```cpp
a = std::move(b); 
```

If move semantics are implemented as a simple swap, then the effect of this is that the objects held by a and b are being exchanged between a and b. Nothing is being destructed yet. The object formerly held by a will of course be destructed eventually, namely, when b goes out of scope. Unless, of course, b becomes the target of a move, in which case the object formerly held by a gets passed on again. Therefore, as far as the implementer of the copy assignment operator is concerned, it is not known when the object formerly held by a will be destructed.

So in a sense, we have drifted into the netherworld of non-deterministic destruction here: a variable has been assigned to, but the object formerly held by that variable is still out there somewhere. That's fine as long as the destruction of that object does not have any side effects that are visible to the outside world. But sometimes destructors do have such side effects. An example would be the release of a lock inside a destructor. Therefore, any part of an object's destruction that has side effects should be performed explicitly in the rvalue reference overload of the copy assignment operator:

```cpp
X& X::operator=(X&& rhs)
{

  // Perform a cleanup that takes care of at least those parts of the
  // destructor that have side effects. Be sure to leave the object
  // in a destructible and assignable state.

  // Move semantics: exchange content between this and rhs
  
  return *this;
}
```

### Is an Rvalue reference an Rvalue?

As before, let X be a class for which we have overloaded the copy constructor and copy assignment operator to implement move semantics. Now consider:

```cpp
void foo(X&& x)
{
  X anotherX = x;
  // ...
}
```

The interesting question is: which overload of X's copy constructor gets called in the body of foo? Here, x is a variable that is declared as an rvalue reference, that is, a reference which preferably and typically (although not necessarily!) refers to an rvalue. Therefore, it is quite plausible to expect that x itself should also bind like an rvalue, that is,

```cpp
X(X&& rhs);
```

should be called. In other words, one might expect that anything that is declared as an rvalue reference is itself an rvalue. The designers of rvalue references have chosen a solution that is a bit more subtle than that:

> Things that are declared as rvalue reference can be lvalues or rvalues. The distinguishing criterion is: if it has a name, then it is an lvalue. Otherwise, it is an rvalue.

In the example above, the thing that is declared as an rvalue reference has a name, and therefore, it is an lvalue:

```cpp
void foo(X&& x)
{
  X anotherX = x; // calls X(X const & rhs)
}
```

Here is an example of something that is declared as an rvalue reference and does not have a name, and is therefore an rvalue:

```cpp
X&& goo();
X x = goo(); // calls X(X&& rhs) because the thing on
             // the right hand side has no name

```

And here's the rationale behind the design: Allowing move sematics to be applied tacitly to something that has a name, as in

```cpp
 X anotherX = x;
  // x is still in scope!
```

would be dangerously confusing and error-prone because the thing from which we just moved, that is, the thing that we just pilfered, is still accessible on subsequent lines of code. But the whole point of move semantics was to apply it only where it "doesn't matter," in the sense that the thing from which we move dies and goes away right after the moving. Hence the rule, "If it has a name, then it's an lvalue."

So then what about the other part, "If it does not have a name, then it's an rvalue?" Looking at the goo example above, it is technically possible, though not very likely, that the expression goo() in the second line of the example refers to something that is still accessible after it has been moved from. But recall from the previous section: sometimes that's what we want! We want to be able to force move semantics on lvalues at our discretion, and it is precisely the rule, "If it does not have a name, then it's an rvalue" that allows us to achieve that in a controlled manner. That's how the function std::move works. Although it is still too early to show you the exact implementation, we just got a step closer to understanding std::move. It passes its argument right through by reference, doing nothing with it at all, and its result type is rvalue reference. So the expression

```cpp
std::move(x)
```

is declared as an rvalue reference and does not have a name. Hence, it is an rvalue. Thus, std::move "turns its argument into an rvalue even if it isn't," and it achieves that by "hiding the name."

For a good example, read it [here](https://thbecker.net/articles/rvalue_references/section_05.html).

### Move Semantics and Compiler Optimizations

Consider the following function definition:

```cpp
X foo()
{
  X x;
  // perhaps do something to x
  return x;
}
```

Now suppose that as before, X is a class for which we have overloaded the copy constructor and copy assignment operator to implement move semantics. If you take the function definition above at face value, you may be tempted to say, wait a minute, there is a value copy happening here from x to the location of foo's return value. Let me make sure we're using move semantics instead:

```cpp
X foo()
{
  X x;
  // perhaps do something to x
  return std::move(x); // making it worse!
}
```

Unfortunately, that would make things worse rather than better. Any modern compiler will apply return value optimization to the original function definition. In other words, rather than constructing an X locally and then copying it out, the compiler would construct the X object directly at the location of foo's return value. Rather obviously, that's even better than move semantics.


### Perfect Forwarding: The problem

Consider the following simple factory function:

```cpp
template<typename T, typename Arg> 
shared_ptr<T> factory(Arg arg)
{ 
  return shared_ptr<T>(new T(arg));
} 
```

obviously, the intent here is to forward the argument arg from the factory function to T's constructor. 
Ideally, as far as arg is concerned, everything should behave just as if the factory function weren't there and the constructor were called directly in the client code: perfect forwarding. The code above fails miserably at that: it introduces an extra call by value, which is particularly bad if the constructor takes its argument by reference.

The most common solution, chosen e.g. by boost::bind, is to let the outer function take the argument by reference:

```cpp
template<typename T, typename Arg> 
shared_ptr<T> factory(Arg& arg)
{ 
  return shared_ptr<T>(new T(arg));
} 
```

That's better, but not perfect. The problem is that now, the factory function cannot be called on rvalues:

```cpp
factory<X>(hoo()); // error if hoo returns by value
factory<X>(41); // error
```

This can be fixed by providing an overload which takes its argument by const reference:

```cpp
template<typename T, typename Arg> 
shared_ptr<T> factory(Arg const & arg)
{ 
  return shared_ptr<T>(new T(arg));
} 
```

There are two problems with this approach. Firstly, if factory had not one, but several arguments, you would have to provide overloads for all combinations of non-const and const reference for the various arguments. Thus, the solution scales extremely poorly to functions with several arguments.

Secondly, this kind of forwarding is less than perfect because it blocks out move semantics: the argument of the constructor of T in the body of factory is an lvalue. Therefore, move semantics can never happen even if it would without the wrapping function.

### Perfect Forwarding: The Solution

Reference collapsing rules

- A& & becomes A&
- A& && becomes A&
- A&& & becomes A&
- A&& && becomes A&&


### References

- [C++ Rvalue References Explained](https://thbecker.net/articles/rvalue_references/section_01.html)
