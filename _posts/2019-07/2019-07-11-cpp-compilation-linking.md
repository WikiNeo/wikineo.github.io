---
title:  "C++ Compilation and Linking"
published: true
tags: C++
---


The compilation of a C++ program involves three steps:

1. Preprocessing: the preprocessor takes a C++ source code file and deals with the
   `#include`, `#define` and other preprocessor directives. The output of this step is
   "pure" C++ file without pre-processor directives.
2. Compilation: the compiler takes the pre-processor's output and produces an object file
   from it.
3. Linking: the linker takes the object files procduced by the compiler and produces
   either a library or an executable file.

## Preprocessing

The preprocessor handles the *preprocessor directives*, like `#include` and `#define`. It
is agnostic of the syntax of C++, which is why it must be used with care.

It works on one C++ source file at a time by replacing `#include` directives with the
content of the respective files (which is usually just declarations), doing replaccement
of macros (`#define`), and selecting different portions of text depending of `#if`,
`#ifdef` and `#ifndef` directives.

The preprocessor works on a stream of preprocessing tokens. Macro subsititution is defined
as replacing tokens with other tokens (the operator `##` enables merging two tokens when
it makes sense).

After all this, the preprocessor produces a single output that is stream of tokens
resulting from the transformations described above. It also adds some special markers that
tell the compiler where each line came from so that it can use those to produce sensible
error messages.

Some errors can be produced at this stage with clever use of the `#if` and `#error`
directives.

## Compilation

The compilation step is performed on each output of the preprocecssor. The compiler parses
the pure C++ source code (now without any preprocessor directives) and convert it into
assembly code. Then invokes underlying back-end (assembler in toolchain) that assembles
that code into machine code producing actual binary file in some format (ELF, COFF, a.out,
...). This object file ontains the compiled code (in binary form) of the symbols defined
in the input. Symbols in object files are referred to by name.

Object files can refer to symbols that are not defined. This is the case when you use a
declaration, and don't provide a definition for it. The compiler doesn't mind this, and
will happily producce the object fle as long as the source code is well-formed.

Compiler usually let you stop compilation at this point. This is very useful because with
it you an compile each source code file separately. The advantage this prodives is that
you don't need to recomiple *everything* if you only change a single file.

The produced object files can be put in special archives called static libraries, for
easier reusing later on.

It's at this sage that "regular" compiler errors, like syntax errors or failed overload
resolution errors, are reported.

## Linking

The linker is what produces the file compilation output from the object files the compiler
produced. This output can be either a shared (or dynamic) library (and while the name is
similar, they haven't got much in common with static libraries mentioned earlier) or an
executable.

It links all the object files by replacing the references to the undefined symbols with
the correct addresses. Each of these symbols can be defined in other object files or in
libraries. If they are defined in libraries other than the standard library, you need to
tell the linked about them.

At this stage the most common errors are missing definitions or duplicate definitions. The
former means that either the definitions don't exist (i.e. they are not written), or that
the object files or libraries where they reside were not given to the linker. The latter
is obvious: the same sybmol was defined in two different object files or libraries.

Reference:
https://stackoverflow.com/questions/6264249/how-does-the-compilation-linking-process-work
