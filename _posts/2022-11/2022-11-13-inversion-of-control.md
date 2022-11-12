---
title: 'Inversion of Control'
published: true
tags: ProgrammingLanguage
---

In software engineering, inversion of control (IoC) is a programming
principle. IoC inverts the flow of control as compared to traditional control
flow. In IoC, custom-written portions of a computer program receive the flow
of control from a generic framework. A software architecture with this design
inverts control as compared to traditional procedural programming: in
traditional programming, the custom code that expresses the purpose of the
program calls into reusable libraries to take care of generic tasks, but with
inversion of control, it is the framework that calls into the custom, or
task-specific, code.

Inversion of control is used to increase modularity of the program and make it
extensible,[1] and has applications in object-oriented programming and other
programming paradigms. The term was used by Michael Mattsson in a thesis,[2]
taken from there[3] by Stefano Mazzocchi and popularized by him in 1999 in a
defunct Apache Software Foundation project, Avalon, then further popularized
in 2004 by Robert C. Martin and Martin Fowler.

The term is related to, but different from, the dependency inversion
principle, which concerns itself with decoupling dependencies between
high-level and low-level layers through shared abstractions. The general
concept is also related to event-driven programming in that it is often
implemented using IoC so that the custom code is commonly only concerned with
the handling of events, whereas the event loop and dispatch of events/messages
is handled by the framework or the runtime environment.

## Reference

- [https://en.wikipedia.org/wiki/Inversion_of_control](https://en.wikipedia.org/wiki/Inversion_of_control)