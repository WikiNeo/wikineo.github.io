---
title: "Duck typing"
published: true
tags: ProgrammingLanguage
---

Duck typing in computer programming is an application of the duck test—"If it
walks like a duck and it quacks like a duck, then it must be a duck"—to
determine whether an object can be used for a particular purpose. With
nominative typing, an object is of a given type if it is declared to be (or if
a type's association with the object is inferred through mechanisms such as
object inheritance). In duck typing, an object is of a given type if it has
all methods and properties required by that type. Duck typing can be
viewed as a usage-based structural equivalence between a given object and the
requirements of a type. See structural typing for a further explanation of
structural type equivalence.

## Example

This is a simple example in Python 3 that demonstrates how any object may be used in any context, up until it is used in a way that it does not support.

```python
class Duck:
    def swim(self):
        print("Duck swimming")

    def fly(self):
        print("Duck flying")

class Whale:
    def swim(self):
        print("Whale swimming")

for animal in [Duck(), Whale()]:
    animal.swim()
    animal.fly()
```

OUtput:

```shell
Duck swimming
Duck flying
Whale swimming
AttributeError: 'Whale' object has no attribute 'fly'
```

So, if we assume everything that can swim is a duck because ducks can swim, we
will consider a whale to be a duck, but, if we also assume it has to be
capable of flying, the whale won’t be considered to be a duck.

## Reference

- [https://en.wikipedia.org/wiki/Duck_typing](https://en.wikipedia.org/wiki/Duck_typing)