---
title:  "C++ Value Categories"
published: true
tags: C++
---

Each C++ expression is characterized by two independent properties: a type and a value category. Each Expression has some non-reference type, and each experssion
belongs to exactly one  of the three primary value categories: prvalue, xvalue, and lvalue, defined as follows:

- a glvalue ("generalized" lvalue) is an expression whose evaluation determines the identity of an object, bit-field, or function;
- a prvalue ("pure rvalue) is an expression whose evaluation either
  - computes the value of the operand of an operator (such prvalue has no result object), or
  - initializes an object or a bit-field (such prvalue is said to have a result object)
- an xvalue (an "eXpiring" value) is a glvalue that denotes an object or bit-field whose resources can be reused
- an lvalue is a gvalue that is not an xvalue
- an rvalue is a prvalue or an xvalue

