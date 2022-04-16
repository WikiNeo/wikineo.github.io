---
title: '[Creational] Simple Factory'
published: true
tags: DesignPattern
---

## Real world example

Consider, you are building a house and you need doors. You can either put on
your carpenter clothes, bring some wood, glue, nails and all the tools
required to build the door and start building it in your house or you can
simply call the factory and get the built door delivered to you so that you
don't need to learn anything about the door making or to deal with the mess
that comes with making it.

## In plain words

Simple factory simply generates an instance for client without exposing any
instantiation logic to the client

## Wikipedia says

In object-oriented programming (OOP), a factory is an object for creating
other objects – formally a factory is a function or method that returns
objects of a varying prototype or class from some method call, which is
assumed to be "new".

## Programmatic Example

First of all we have a door interface and the implementation

```typescript
interface Door {
    getWidth(): number;
    getHeight(): number
}

class WoodenDoor implements Door {
    protected width;
    protected height;

    constructor(width: number, height: number) {
        this.width = width;
        this.height = height;
    }

    getWidth(): number {
        return this.width;
    }

    getHeight(): number {
        return this.height;
    }
}
```

Then we have our door factory that makes the door and returns it

```typescript
class DoorFactory {
    static makeDoor(width: number, height: number): Door{
        return new WoodenDoor(width, height);
    }
}

```

And then it can be used as

```typescript
let door: Door = DoorFactory.makeDoor(100, 200);
console.log(door.getWidth())
console.log(door.getHeight())

let door2: Door = DoorFactory.makeDoor(50, 100)
```

## When to Use?

When creating an object is not just a few assignments and involves some logic,
it makes sense to put it in a dedicated factory instead of repeating the same
code everywhere.

## References

- [https://github.com/kamranahmedse/design-patterns-for-humans](https://github.com/kamranahmedse/design-patterns-for-humans)
- [https://github.com/torokmark/design_patterns_in_typescript](https://github.com/torokmark/design_patterns_in_typescript)
- [https://refactoring.guru/design-patterns](https://refactoring.guru/design-patterns)