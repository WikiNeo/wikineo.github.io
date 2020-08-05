---
title: "Single Responsibility Principle"
published: true
tags: DesignPattern
---

The single responsibility principle is a computer programming principle that
states that every module, class, or function should have responsibility over a
single part of functionality provided by the software, and that responsibility
should be entirely encapsulated by the class, module or function. All its
services should be narrowly aligned with that responsibility.

## Example

Martin defines a responsibility as a reason to change, and concludes that a
class or module should have one, and only one, reason to be changed (i.e.
rewritten). As an example, consider a module that compiles and prints a report.
Imagine such a module that can be changed for two reasons. First, the content of
the report could change. Second, the format of the report could change. These
two things change for very different causes; These two things change for very
different causes; one substantive, and one cosmetic. The single responsibility
principle says that these two aspects of the problem are really two separate
responsibilities, and should therefore be in separate classes or modules. It
would be a bad design to couple two things that change for different reasons at
different times.

The reasons it is so important to keep a class focused on a single concern is
that it makes the class more robust. Continuing with the foregoing example, if
there is a change to the report compilation process, there is greater danger
that the printing code will break if it is part of the same class.

References:

- [https://en.wikipedia.org/wiki/Single_responsibility_principle](https://en.wikipedia.org/wiki/Single_responsibility_principle)