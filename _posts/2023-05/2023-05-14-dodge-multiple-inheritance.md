---
title: "Dodge: Multiple Inheritance"
published: true
tags: DesignPattern
---

Some Python projects fall short of practicing Composition Over Inheritance
because they are tempted to dodge the principle by means of a controversial
feature of the Python language: multiple inheritance.

Let’s return to the example code we started with, where `FilteredLogger` and
`SocketLogger` were two different subclasses of a base `Logger` class. In a
language that only supported single inheritance, a `FilteredSocketLogger` would
have to choose to inherit either from `SocketLogger` or `FilteredLogger`, and
would then have to duplicate code from the other class.

But Python supports multiple inheritance, so the new `FilteredSocketLogger` can
list both `SocketLogger` and `FilteredLogger` as base classes and inherit from
both:

```python
# Our original example’s base class and subclasses.

class Logger(object):
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message + '\n')
        self.file.flush()

class SocketLogger(Logger):
    def __init__(self, sock):
        self.sock = sock

    def log(self, message):
        self.sock.sendall((message + '\n').encode('ascii'))

class FilteredLogger(Logger):
    def __init__(self, pattern, file):
        self.pattern = pattern
        super().__init__(file)

    def log(self, message):
        if self.pattern in message:
            super().log(message)

# A class derived through multiple inheritance.

class FilteredSocketLogger(FilteredLogger, SocketLogger):
    def __init__(self, pattern, sock):
        FilteredLogger.__init__(self, pattern, None)
        SocketLogger.__init__(self, sock)

# Works just fine.

logger = FilteredSocketLogger('Error', sock1)
logger.log('Warning: not that important')
logger.log('Error: this is important')

print('The socket received: %r' % sock2.recv(512))
```

```shell
The socket received: b'Error: this is important\n'
```

This bears several striking resemblances to our Decorator Pattern solution. In both cases:

- There’s a logger class for each kind of output (instead of our Adapter’s asymmetry between writing files directly but non-files through an adapter).
- The `message` preserves the exact value provided by the caller (instead of our Adapter’s habit of replacing it with a file-specific value by appending a newline).
- The filter and loggers are symmetric in that they both implement the same method `log()`. (Our other solutions besides the Decorator had filter classes offering one method and output classes offering another).
- The filter never tries to produce output on its own but, if a message survives filtering, defers the task of output to other code.

These close similarities with our earlier Decorator solution mean that we can compare it with this new code to make an unusually sharp comparison between Composition Over Inheritance and multiple inheritance. Let’s sharpen the focus still further with a question:

*If we have thorough unit tests for both the logger and filter, how confident are we that they will work together?*

1. The success of the Decorator example depends only on the public behaviors of
each class: that the `LogFilter` offers a `log()` method that in turn calls `log()`
on the object it wraps (which a test can trivially verify using a tiny fake
logger), and that each logger offers a working `log()` method. As long as our
unit tests verify these two public behaviors, we can’t break composition
without failing our unit tests.

    Multiple inheritance, by contrast, depends on behavior that cannot be verified
by simply instantiating the classes in question. The public behavior of a
`FilteredLogger` is that it offers a `log()` method that both filters and writes
to a file. But multiple inheritance doesn’t merely depend on that public
behavior, but on how that behavior is implemented internally. Multiple
inheritance will work if the method is deferring to its base class using
`super()`, but not if the method does its own `write()` to the file, even though
either implementation would satisfy the unit test.

    A test suite must therefore go beyond unit testing and perform actual multiple
inheritance on the class — or else monkey patch to verify that `log()` calls
`super().log()` — to guarantee that multiple inheritance keeps working as future
developers work on the code.

2. Multiple inheritance has introduced a new `__init__()` method because neither
base class’s `__init__()` method accepts enough arguments for a combined filter
and logger. That new code needs to be tested, so at least one test will be
necessary for every new subclass.

    You might be tempted to concoct a scheme to avoid a new `__init__()` for every
subclass, like accepting `*args` and then passing them on to `super().__init__()`.
(If you do pursue that approach, review the classic essay “Python’s Super
Considered Harmful” which argues that only `**kw` is in fact safe.) The problem
with such a scheme is that it hurts readability — you can no longer figure out
what arguments an `__init__()` method takes simply by reading its parameter
list. And type checking tools will no longer be able to guarantee correctness.

    But whether you give each derived class its own `__init__()` or design them to
chain together, your unit tests of the original `FilteredLogger` and
`SocketLogger` can’t by themselves guarantee that the classes initialize
correctly when combined.

    By contrast, the Decorator’s design leaves its initializers happily and
strictly orthogonal. The filter accepts its `pattern`, the logger accepts its
`sock`, and there is no possible conflict between the two.

3. Finally, it’s possible that two classes work fine on their own, but have class
or instance attributes with the same name that will collide when the classes
are combined through multiple inheritance.

    Yes, our small examples here make the chance of collision look too small to
worry about — but remember that these examples are merely standing in for the
vastly more complicated classes you might write in real applications.

    Whether the programmer writes tests to guard against collision by running
`dir()` on instances of each class and checking for attributes they have in
common, or by writing an integration test for every possible subclass, the
original unit tests of the two separate classes will once again have failed to
guarantee that they can combine cleanly through multiple inheritance.

For any of these reasons, the unit tests of two base classes can stay green
even as their ability to be combined through multiple inheritance is broken.
This means that the Gang of Four’s “explosion of subclasses to support every
combination” will also afflict your tests. Only by testing every combination
of m×n base classes in your application can you make it safe for the
application to use such classes at runtime.

In addition to breaking the guarantees of unit testing, multiple inheritance
involves at least three further liabilities.

1. Introspection is simple in the Decorator case. Simply `print(my_filter.logger)`
or view that attribute in a debugger to see what sort of output logger is
attached. In the case of multiple inheritance, however, you can only learn
which filter and logger have been combined by examining the metadata of the
class itself — either by reading its `__mro__` or subjecting the object to a
series of `isinstance()` tests.

2. It’s trivial in the Decorator case to take a live combination of a filter and
logger and at runtime to swap in a different logger through assignment to the
`.logger` attribute — say, because the user has just toggled a preference in the
application’s interface. But to do the same in the multiple inheritance case
would require the rather more objectionable maneuver of overwriting the
object’s class. While changing an object’s class at runtime is not impossible
in a dynamic language like Python, it’s generally considered a symptom that
software design has gone wrong.

3. Finally, multiple inheritance provides no built-in mechanism to help the
programmer order the base classes correctly. The `FilteredSocketLogger` won’t
successfully write to a socket if its base classes are swapped and, as dozens
of Stack Overflow questions attest, Python programmers have perpetual
difficultly with putting third-party base classes in the right order. The
Decorator pattern, by contrast, makes it obvious which way the classes
compose: the filter’s `__init__()` wants a `logger` object, but the logger’s
`__init__()` doesn’t ask for a `filter`.

Multiple inheritance, then, incurs a number of liabilities without adding a
single advantage. At least in this example, solving a design problem with
inheritance is strictly worse than a design based on composition.

## Reference

- [https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-multiple-inheritance](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-multiple-inheritance)