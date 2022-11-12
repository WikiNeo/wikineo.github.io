---
title: 'Constant Folding'
published: true
tags: ProgrammingLanguage
---

Constant folding is the process of recognizing and evaluating constant
expressions at compile time rather than computing them at runtime. Terms in
constant expressions are typically simple literals, such as the integer
literal `2`, but they may also be variables whose values are known at compile
time. Consider the statement:

```javascript
i = 320 * 200 * 32;
```

Most compilers would not actually generate two multiply instructions and a
store for this statement. Instead, they identify constructs such as these and
substitute the computed values at compile time (in this case, `2,048,000`).

Constant folding can make use of arithmetic identities. If x is numeric, the
value of `0 * x` is zero even if the compiler does not know the value of `x` (note
that this is not valid for IEEE floats since `x` could be Infinity or
NotANumber. Still, some languages that favor performance such as GLSL allow
this for constants, which can occasionally cause bugs).

Constant folding may apply to more than just numbers. Concatenation of string
literals and constant strings can be constant folded. Code such as `"abc" +
"def"` may be replaced with `"abcdef"`.

## Reference

- [https://en.wikipedia.org/wiki/Constant_folding](https://en.wikipedia.org/wiki/Constant_folding)