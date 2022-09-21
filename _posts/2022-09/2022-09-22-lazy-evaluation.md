---
title: 'Lazy evaluation'
published: true
tags: ProgrammingLanguage
---

In programming language theory, lazy evaluation, or call-by-need, is an
evaluation strategy which delays the evaluation of an expression until its
value is needed (non-strict evaluation) and which also avoids repeated
evaluations (sharing).

The benefits of lazy evaluation include:

- The ability to define control flow (structures) as abstractions instead of primitives.
- The ability to define potentially infinite data structures. This allows for more straightforward implementation of some algorithms.
- The ability to define partially-defined data structures where some elements
  are errors. This allows for rapid prototyping.

Lazy evaluation is often combined with memoization, as described in Jon
Bentley's Writing Efficient Programs. After a function's value is computed
for that parameter or set of parameters, the result is stored in a lookup
table that is indexed by the values of those parameters; the next time the
function is called, the table is consulted to determine whether the result for
that combination of parameter values is already available. If so, the stored
result is simply returned. If not, the function is evaluated and another entry
is added to the lookup table for reuse.

Lazy evaluation is difficult to combine with imperative features such as
exception handling and input/output, because the order of operations becomes
indeterminate.

The opposite of lazy evaluation is eager evaluation, sometimes known as strict
evaluation. Eager evaluation is the evaluation strategy employed in
most programming languages.

## Reference

- [https://en.wikipedia.org/wiki/Lazy_evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation)