---
title: '[Creational] Singleton'
published: true
tags: DesignPattern
---

## Real world example

There can only be one president of a country at a time. The same president has
to be brought to action, whenever duty calls. President here is singleton.

## In plain words

Ensures that only one object of a particular class is ever created.

## Wikipedia says

In software engineering, the singleton pattern is a software design pattern
that restricts the instantiation of a class to one object. This is useful when
exactly one object is needed to coordinate actions across the system.

Singleton pattern is actually considered an anti-pattern and overuse of it
should be avoided. It is not necessarily bad and could have some valid
use-cases but should be used with caution because it introduces a global state
in your application and change to it in one place could affect in the other
areas and it could become pretty difficult to debug. The other bad thing about
them is it makes your code tightly coupled plus mocking the singleton could be
difficult.

## Programmatic Example

To create a singleton, make the constructor private, disable cloning, disable
extension and create a static variable to house the instance

```typescript
class Singleton {
    private static singleton: Singleton;

    // disable constructor with private
    private constructor() {
    }

    public static getInstance(): Singleton {
        if(!Singleton.singleton){
            Singleton.singleton = new Singleton();
        }
        return Singleton.singleton;
    }
}

const singleton1 = Singleton.getInstance();
const singleton2 = Singleton.getInstance();

console.log(singleton1 === singleton2)  // true
```

## References

- [https://github.com/kamranahmedse/design-patterns-for-humans](https://github.com/kamranahmedse/design-patterns-for-humans)
- [https://github.com/torokmark/design_patterns_in_typescript](https://github.com/torokmark/design_patterns_in_typescript)
- [https://refactoring.guru/design-patterns](https://refactoring.guru/design-patterns)