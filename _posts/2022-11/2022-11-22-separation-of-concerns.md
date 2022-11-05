---
title: 'Separation of Concerns'
published: true
tags: DesignPattern
---

In computer science, separation of concerns is a design principle for
separating a computer program into distinct sections. Each section addresses a
separate concern, a set of information that affects the code of a computer
program. A concern can be as general as "the details of the hardware for an
application", or as specific as "the name of which class to instantiate". A
program that embodies SoC well is called a modular[1] program. Modularity, and
hence separation of concerns, is achieved by encapsulating information inside
a section of code that has a well-defined interface. Encapsulation is a means
of information hiding.[2] Layered designs in information systems are another
embodiment of separation of concerns (e.g., presentation layer, business logic
layer, data access layer, persistence layer).[3]

Separation of concerns results in more degrees of freedom for some aspect of
the program's design, deployment, or usage. Common among these is increased
freedom for simplification and maintenance of code. When concerns are
well-separated, there are more opportunities for module upgrade, reuse, and
independent development. Hiding the implementation details of modules behind
an interface enables improving or modifying a single concern's section of code
without having to know the details of other sections and without having to
make corresponding changes to those other sections. Modules can also expose
different versions of an interface, which increases the freedom to upgrade a
complex system in piecemeal fashion without interim loss of
functionality.

Separation of concerns is a form of abstraction. As with most abstractions,
separating concerns means adding additional code interfaces, generally
creating more code to be executed. So despite the many benefits of
well-separated concerns, there is often an associated execution penalty.

## Reference

- [https://en.wikipedia.org/wiki/Separation_of_concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)