---
title: 'Makefile Symbols'
published: true
tags: Makefile
---

`$@` is the name of the target being generated, and `$<` the first prerequisite
(usually a source file). You can find a list of all these special variables in
the GNU Make manual.

For example, consider the following declaration:

```makefile
all: library.cpp main.cpp
```

In this case:

- `$@` evaluates to `all`
- `$<` evaluates to `library.cpp`
- `$^` evaluates to `library.cpp main.cpp`


## Reference

- [https://stackoverflow.com/questions/3220277/what-do-the-makefile-symbols-and-mean](https://stackoverflow.com/questions/3220277/what-do-the-makefile-symbols-and-mean)