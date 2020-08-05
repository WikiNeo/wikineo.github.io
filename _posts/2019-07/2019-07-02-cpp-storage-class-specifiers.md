---
title:  "C++ Storage Class Specifiers"
published: true
tags: C++
---

The storage class specifiers are a part of the decl-specifier-seq of a name's declaration syntax. Together with the scope of the name,
they control two independent properties of the name: its storage duration and its linkage.

- auto - automatic storage duration. (until C++11)
- register - automatic storage duration. Also hints the compiler to place the object in the processor's register. (deprecated) (unitl C++17)
- static - static or thread storage duration and internal linkage.
- extern - static or thread storage duration and external linkage.
- thread_local - thread storage duration. (since C++11)
- mutable - does not affect storage duration or linkage.

## Storage duration

- automatic storage duration. The storage for the object is allocated at the beginning of the enclosing code block and deallocated at the end. All local objects have this storage duration, except those declared static, extern or thread local.
- static storage duration. The storage for the object is allocated when then program begins and deallocated when the program ends. Only one instance of the object exists. All objects declared at namespace scopre (including global namespace) have this storage duration, pluse those declared with satic or extern.
- thread storage duration. The storage for the object is allocated when the thread begins and deallocated when the thread ends. Each thread has its own instance of the object. Only objects declared thread_local have this storage duration. thread_local can apprear together with static or extern to adjust linkage.
- dynamic storage duration. The storage for the object is allocated and deallocated per request by using dynamic memory allocation functions.


