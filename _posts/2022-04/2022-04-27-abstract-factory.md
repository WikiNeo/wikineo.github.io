---
title: '[Creational] Abstract Factory'
published: true
tags: DesignPattern
---

## Real world example

Extending our door example from Simple Factory. Based on your needs you might
get a wooden door from a wooden door shop, iron door from an iron shop or a
PVC door from the relevant shop. Plus you might need a guy with different kind
of specialities to fit the door, for example a carpenter for wooden door,
welder for iron door etc. As you can see there is a dependency between the
doors now, wooden door needs carpenter, iron door needs a welder etc.

## In plain words

A factory of factories; a factory that groups the individual but
related/dependent factories together without specifying their concrete
classes.

## Wikipedia says

The abstract factory pattern provides a way to encapsulate a group of
individual factories that have a common theme without specifying their
concrete classes

## Programmatic Example

Translating the door example above. First of all we have our Door interface
and some implementation for it

```typescript
interface Door {
    getDescription();
}

class WoodenDoor implements Door {
    getDescription() {
        console.log('I am a wooden door')
    }
}

class IronDoor implements Door {
    getDescription() {
        console.log('I am a iron door')
    }
}
```

Then we have some fitting experts for each door type

```typescript
interface DoorFittingExpert {
    getDescription();
}

class Welder implements DoorFittingExpert {
    getDescription() {
        console.log('I can only fit iron doors')
    }
}

class Carpenter implements DoorFittingExpert {
    getDescription() {
        console.log('I can only fit wooden doors')
    }
}
```

Now we have our abstract factory that would let us make family of related
objects i.e. wooden door factory would create a wooden door and wooden door
fitting expert and iron door factory would create an iron door and iron door
fitting expert

```typescript
interface DoorFactory {
    makeDoor(): Door;
    makeFittingExpert(): DoorFittingExpert;
}

class WoodenDoorFactory implements DoorFactory {
    makeDoor(): Door {
        return new WoodenDoor()
    }
    makeFittingExpert(): DoorFittingExpert {
        return new Carpenter()
    }
}

class IronDoorFactory implements DoorFactory {
    makeDoor(): Door {
        return new IronDoor();
    }
    makeFittingExpert(): DoorFittingExpert {
        return new Welder()
    }
}
```

And then it can be used as

```typescript
// wooden
const woodenFactory = new WoodenDoorFactory()
let door = woodenFactory.makeDoor();
let expert = woodenFactory.makeFittingExpert()
door.getDescription()
expert.getDescription()

// iron
const ironFactory = new IronDoorFactory()
door = ironFactory.makeDoor()
expert = ironFactory.makeFittingExpert()
door.getDescription()
expert.getDescription()
```

As you can see the wooden door factory has encapsulated the carpenter and the
wooden door also iron door factory has encapsulated the iron door and welder.
And thus it had helped us make sure that for each of the created door, we do
not get a wrong fitting expert.

## When to use?

When there are interrelated dependencies with not-that-simple creation logic involved

## References

- [https://github.com/kamranahmedse/design-patterns-for-humans](https://github.com/kamranahmedse/design-patterns-for-humans)
- [https://github.com/torokmark/design_patterns_in_typescript](https://github.com/torokmark/design_patterns_in_typescript)
- [https://refactoring.guru/design-patterns](https://refactoring.guru/design-patterns)