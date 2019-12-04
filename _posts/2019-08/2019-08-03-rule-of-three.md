---
title:  "Rule of three (C++ programming)"
published: true
categories: tech
tags: C++
---

The rule of three and rule of five and rules of thumb in C++ for the building of
exception-safe code and for formalizing rules on resource management. It accomplishes this
by prescribing how the default members of a class should be used to accomplish this task
in a systematic manner.

## Rule of Three

The **rule of three** is a rule of thumb in C++ (prior to C++11) that claims that if a
class defines one (or more) of the following it should probably explicitly define all
three:

- destructor
- copy constructor
- copy assignment operator

## Rule of Five

With the advent of C++11 the rule of three can be broadened to the *rule of five* as C++
implements move semantics.

- destructor
- copy constructor
- copy assignment operator
- move constructor
- move assignment operator

References: [https://en.wikipedia.org/wiki/Rule_of_three_(C%2B%2B_programming)](https://en.wikipedia.org/wiki/Rule_of_three_(C%2B%2B_programming))
