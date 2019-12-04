---
title:  "C++ Virtual Base Class"
published: true
categories: tech
tags: C++
---

Virtual base classes, used in virtual inheritance, is a way of preventing multiple
"instances" of a given class appearing in an inheritance hierarchy when using multiple
inheritance.

```cpp
class A { public: void foo () {} };
class B : public A {};
class C : public A {};
class D : public B, public C {};

D d;
d.Foo();    // There will be two instances of A, and is this B's foo() or C's?
```

With virtual, there is only one instance of A

```cpp
class A { public: void Foo() {} };
class B : public virtual A {};
class C : public virtual A {};
class D : public B, public C {};

D d;
d.foo();    // no longer ambiguous
```

References: [https://stackoverflow.com/questions/21558/in-c-what-is-a-virtual-base-class](https://stackoverflow.com/questions/21558/in-c-what-is-a-virtual-base-class)
