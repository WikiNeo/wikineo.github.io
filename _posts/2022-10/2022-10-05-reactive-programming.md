---
title: 'Reactive Programming'
published: true
tags: ProgrammingLanguage
---

In computing, reactive programming is a declarative programming paradigm
concerned with data streams and the propagation of change. With this paradigm,
it's possible to express static (e.g., arrays) or dynamic (e.g., event
emitters) data streams with ease, and also communicate that an inferred
dependency within the associated execution model exists, which facilitates the
automatic propagation of the changed data flow.

For example, in an imperative programming setting, `a := b + c` would mean that
`a` is being assigned the result of `b + c` in the instant the expression is
evaluated, and later, the values of `b` and `c` can be changed with no effect on
the value of `a`. On the other hand, in reactive programming, the value of `a` is
automatically updated whenever the values of `b` or `c` change, without the
program having to explicitly re-execute the statement `a := b + c` to determine
the presently assigned value of `a`.

```javascript
var b = 1
var c = 2
var a = b + c
b = 10
console.log(a) // 3 (not 12 because "=" is not a reactive assignment operator)

// now imagine you have a special operator "$=" that changes the value of a variable (executes code on the right side of the operator and assigns result to left side variable) not only when explicitly initialized, but also when referenced variables (on the right side of the operator) are changed
var b = 1
var c = 2
var a $= b + c
b = 10
console.log(a) // 12
```

Another example is a hardware description language such as Verilog, where
reactive programming enables changes to be modeled as they propagate through
circuits.

Reactive programming has been proposed as a way to simplify the creation of
interactive user interfaces and near-real-time system animation.

For example, in a model–view–controller (MVC) architecture, reactive
programming can facilitate changes in an underlying model that are reflected
automatically in an associated view.

## Reference

- [https://en.wikipedia.org/wiki/Reactive_programming](https://en.wikipedia.org/wiki/Reactive_programming)