---
title:  "C++ Named Requirements Basic"
published: false
tags: C++
---

The named requirements are used in the normative text of the C++ standard to define the 
expectations of the standard library.

## DefaultConstructible

Specifies that an object of the type can be default constructed

### Requiements

The type T sastifies DefaultConstuctible if given u, an arbitrary identifier, the following expressions must be valid and have their specified effects

|Expression|Post-conditions|
|`T u`|The object us is default-initialized|
