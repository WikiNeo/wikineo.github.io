---
title: 'Programming Paradigms'
published: true
tags: ProgrammingLanguage
---

Programming paradigms are a way to classify programming languages based on their features. Languages can be classified into multiple paradigms.

Some paradigms are concerned mainly with implications for the execution model of the language, such as allowing side effects, or whether the sequence of operations is defined by the execution model. Other paradigms are concerned mainly with the way that code is organized, such as grouping a code into units along with the state that is modified by the code. Yet others are concerned mainly with the style of syntax and grammar.

Common programming paradigms include:

- imperative in which the programmer instructs the machine how to change its state,
  - procedural which groups instructions into procedures,
  - object-oriented which groups instructions with the part of the state they operate on,
- declarative in which the programmer merely declares properties of the desired result, but not how to compute it
  - functional in which the desired result is declared as the value of a series of function applications,
  - logic in which the desired result is declared as the answer to a question about a system of facts and rules,
  - mathematical in which the desired result is declared as the solution of an optimization problem
  - reactive in which the desired result is declared with data streams and the
    propagation of change

Symbolic techniques such as reflection, which allow the program to refer to itself, might also be considered as a programming paradigm. However, this is compatible with the major paradigms and thus is not a real paradigm in its own right.

For example, languages that fall into the imperative paradigm have two main features: they state the order in which operations occur, with constructs that explicitly control that order, and they allow side effects, in which state can be modified at one point in time, within one unit of code, and then later read at a different point in time inside a different unit of code. The communication between the units of code is not explicit. Meanwhile, in object-oriented programming, code is organized into objects that contain a state that is only modified by the code that is part of the object. Most object-oriented languages are also imperative languages. In contrast, languages that fit the declarative paradigm do not state the order in which to execute operations. Instead, they supply a number of available operations in the system, along with the conditions under which each is allowed to execute.[4] The implementation of the language's execution model tracks which operations are free to execute and chooses the order independently.

## Reference

- [https://en.wikipedia.org/wiki/Programming_paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)