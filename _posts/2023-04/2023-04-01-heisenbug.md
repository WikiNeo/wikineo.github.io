---
title: "Heisenbug"
published: true
tags: SoftwareEngineering
---

In computer programming jargon, a heisenbug is a software bug that seems to
disappear or alter its behavior when one attempts to study it.[1] The term is
a pun on the name of Werner Heisenberg, the physicist who first asserted the
observer effect of quantum mechanics, which states that the act of observing a
system inevitably alters its state. In electronics, the traditional term is
probe effect, where attaching a test probe to a device changes its behavior.

Similar terms, such as bohrbug, mandelbug,[2][3][4] hindenbug, and
schrödinbug[5][6] (see the section on related terms) have been occasionally
proposed for other kinds of unusual software bugs, sometimes in jest.[7][8]

## Examples

Heisenbugs occur because common attempts to debug a program, such as inserting
output statements or running it with a debugger, usually have the side-effect
of altering the behavior of the program in subtle ways, such as changing the
memory addresses of variables and the timing of its execution.

One common example of a heisenbug is a bug that appears when the program is
compiled with an optimizing compiler, but not when the same program is
compiled without optimization (as is often done for the purpose of examining
it with a debugger). While debugging, values that an optimized program would
normally keep in registers are often pushed to main memory. This may affect,
for instance, the result of floating-point comparisons, since the value in
memory may have smaller range and accuracy than the value in the register.
Similarly, heisenbugs may be caused by side-effects in test expressions used
in runtime assertions in languages such as C and C++, where the test
expression is not evaluated when assertions are turned off in production code
using the NDEBUG macro.

Other common causes of heisenbugs are using the value of a non-initialized
variable (which may change its address or initial value during debugging), or
following an invalid pointer (which may point to a different place when
debugging). Debuggers also commonly allow the use of breakpoints or provide
other user interfaces that cause additional source code (such as property
accessors) to be executed stealthily, which can, in turn, change the state of
the program.[9]

Time can also be a factor in heisenbugs, particularly with multi-threaded
applications. Executing a program under control of a debugger can change the
execution timing of the program as compared to normal execution.
Time-sensitive bugs, such as race conditions, may not occur when the program
is slowed down by single-stepping source lines in the debugger. This is
particularly true when the behavior involves interaction with an entity not
under the control of a debugger, such as when debugging network packet
processing between two machines and only one is under debugger control.

Heisenbugs can be viewed as instances of the observer effect in information
technology. Frustrated programmers may humorously blame a heisenbug on the
phase of the moon,[10] or (if it has occurred only once) may explain it away
as a soft error due to alpha particles or cosmic rays affecting the hardware,
a well-documented phenomenon known as single event effects.

## Reference

- [https://en.wikipedia.org/wiki/Heisenbug](https://en.wikipedia.org/wiki/Heisenbug)