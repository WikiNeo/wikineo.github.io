---
title: "Dodge: Building classes dynamically"
published: true
tags: DesignPattern
---

As we saw in the previous two sections, neither traditional multiple
inheritance nor mixins solve the Gang of Four’s problem of “an explosion of
subclasses to support every combination” — they merely avoid code duplication
when two classes need to be combined.

Multiple inheritance still requires, in the general case, “a proliferation of
classes” with m×n class statements that each look like:

```python
class FilteredSocketLogger(FilteredLogger, SocketLogger):
    ...
```

But it turns out that Python offers a workaround.

Imagine that our application reads a configuration file to learn the log
filter and log destination it should use, a file whose contents aren’t known
until runtime. Instead of building all m×n possible classes ahead of time and
then selecting the right one, we can wait and take advantage of the fact that
Python not only supports the `class` statement but a builtin `type()` function
that creates new classes dynamically at runtime:

```python
# Imagine 2 filtered loggers and 3 output loggers.

filters = {
    'pattern': PatternFilteredLog,
    'severity': SeverityFilteredLog,
}
outputs = {
    'file': FileLog,
    'socket': SocketLog,
    'syslog': SyslogLog,
}

# Select the two classes we want to combine.

with open('config') as f:
    filter_name, output_name = f.read().split()

filter_cls = filters[filter_name]
output_cls = outputs[output_name]

# Build a new derived class (!)

name = filter_name.title() + output_name.title() + 'Log'
cls = type(name, (filter_cls, output_cls), {})

# Call it as usual to produce an instance.

logger = cls(...)
```

The tuple of classes passed to `type()` has the same meaning as the series of
base classes in a `class` statement. The `type()` call above creates a new class
through multiple inheritance from both a filtered logger and an output logger.

Before you ask: yes, it would also work to build a `class` statement as plain
text and then pass it to `eval()`.

But building classes on-the-fly carries severe liabilities.

- Readability suffers. A human reading the above snippet of code will have to do
extra work to determine what sort of object an instance of `cls` is. Also, many
Python programmers aren’t familiar with `type()` and will need to stop and
puzzle over its documentation. If they have difficulty with the novel concept
that classes can be defined dynamically, they might still be confused.

- If a constructed class like `PatternFilteredFileLog` is named in an exception or
error message, the developer will probably be unhappy to discover that nothing
comes up when they search the code for that class name. Debugging becomes more
difficult when you cannot even locate a class. Considerable time may be spent
searching the codebase for `type()` calls and trying to determine which one
generated the class. Sometimes developers have to resort to calling each
method with bad arguments and using the line numbers in the resulting
tracebacks to track down the base classes.

- Type introspection will, in the general case, fail for classes constructed
dynamically at runtime. “Jump to class” shortcuts in your editor won’t have
anywhere to take you when you highlight an instance of `PatternFilteredFileLog`
in the debugger. And type checking engines like mypy and pyre-check will be
unlikely to offer the strong protections for your generated class that they’re
able to provide for normal Python classes.

- The beautiful Jupyter Notebook feature `%autoreload` possesses a nearly
preternatural ability to detect and reload modified source code in a live
Python interpreter. But it’s foiled, for example, by the multiple inheritance
classes that matplotlib builds at runtime through `type()` calls inside its
`subplot_class_factory()`.

Once its liabilities are weighed, the attempt to use runtime class generation
as a last-ditch maneuver to rescue the already faulty mechanism of multiple
inheritance stands as a reductio ad absurdum of the entire project of dodging
Composition Over Inheritance when you need an object’s behavior to vary over
several independent axes.

## Reference

- [https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-building-classes-dynamically](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-building-classes-dynamically)