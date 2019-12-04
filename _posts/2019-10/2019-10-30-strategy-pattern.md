---
title:  "Strategy Pattern"
published: true
---

## It started with a simple SimUDuck app

SimUDuck is a duck simulation game.

```javascript
Duck {
    // All duck quack and swim, the superclass takes care of the implementation code
    quack()
    swim()

    // the display() method is abstract, since all duck subtypes look different
    display()

    // Other duck-like method
}

MallardDuck extends Duck {
    // Each duck subtype is responsible for implementing its own display() behavior for how
    // it looks on screen
    display(){
        // looks like a mallard
    }
}

RedheadDuck extends Duck {
    display(){
        // looks like a redhead
    }
}

// lots of other types of ducks inherit from the Duck class
```

## But now we need the ducks to FLY

```javascript
Duck {
    // All duck quack and swim, the superclass takes care of the implementation code
    quack()
    swim()

    // the display() method is abstract, since all duck subtypes look different
    display()

    // FLY HERE
    fly()

    // Other duck-like method
}
```

## But something went horribly wrong

- **Rubber duckies** fly.

Not all subclass of Duck should *fly*. When new behavior is added to the `Duck`
superclass, behavior that was not appropriate for some Duck subclasses is also added.

## Thinks about inheritance

- Override `fly()` in subclass

But what happens when we add wooden decoy ducks to the program? They aren't supposed to
fly or quack..

## How about an interface

- `Flyable() interface`

There will be much more duplicated code.

## Zeroing in on the problem

So we know using inheritance hasn't worked out very well, since the duck behavior keeps
changing across the subclasses, and its not appropriate for all subclasses to have those
behaviors.

The Flyable and Quackable interface sounded promising at first -- only ducks that really
do fly will be Flyable, etc. -- except Java interfaces have no implementation code, so no
code reuse. And that means that whenever you need to modify a behavior, you're forced to
track down and change it in all the different subclasses where that behavior is defined,
probably introducing new bugs along the way!

### Design Principle

**Identify the aspects of your application that vary and separate them from what stays the
same.**

Take what varies and "encapsulate" it so it won't affect the rest of your code.

The result? Fewer unintended consequences from code changes and more flexibility in your
system!

Take the parts that vary and encapsulate them, so that later you can alter or extend the
parts that vary without affecting those that don't

## Separating what changes from what stays the same

We know that `fly()` and `quack()` are the parts of the Duck class that vary across ducks.

To separate these behaviors from the Duck class, we'll pull both methods out of the Duck
class and create a new set of classes to represent each behavior.

The Duck class is still the superclass of all ducks, but we are pulling out the fly and
quack behaviors and putting them into another class structure.

Now flying and quacking each get their own set of classes. Various behavior implementation
are going to live here.

## Designing the Duck Behaviors

From now on, the Duck behaviors will live in a separate class - a class that implements a
particular behavior interface.

That way, the Duck classes won't need to know any of the implementation details for their
own behaviors.

### Design Principles

**Program to an interface, not an implementation**

We'll use an interface to represent each behavior - for instance, FlyBehavior and
QuackBehavior - and each implementation of a behavior will implement one of those
interfaces.

So this time it won't be the Duck classes that will implement the flying and quacking
interfaces. Instead, we'll make a set of classes whose entire reason for living is to
represent a behavior (for example, "squeaking"), and it's the behavior class, rathe than
the Duck class, that will implement the behavior interface.

This is in contrast to the way we were doing things before, where a behavior either came
from a concrete implementation in the superclass Duck, or by providing a specialized
implementation in the subclass itself. In both cases, we were relying on an
implementation. We were locked into using that specific implementation and there was no
room for changing out the behavior (other than writing more code).

With our new design, the Duck subclasses will use a behavior represented by an interface
(FlyBehavior and QuackBehavior), so that the actual implementation of the behavior (in
other words, the specific concrete behavior coded in the class that implements the
FlyBehavior or QuackBehavior) won't be locked into the Duck subclass.

#### Programming to an implementation

```javascript
// Declaring the variable "d" as the type Dog (a concrete implementation of Animal) forces us to code to a concrete implementation.
Dog d = new Dog();
d.bark();
```

#### Programming to an interface/supertype

```javascript
// We don't know it's a Dog, but we can now use the animal reference polymorphically.
Animal animal = new Dog();
animal.makeSound();
```

Even better, rather than hard-coding the instantiation of the subtype (like new Dog())
into the code, assign the concrete implementation object at runtime

```javascript
// We don't know WHAT the actual animal subtype is, all we care about is that it knows how to respond to makeSound()
a = getAnimal();
a.makeSound();
```

## Implementing the Duck Behaviors

With this design, other types of objects can reuse our fly and quack be behaviors because
these behaviors are no longer hidden away in our Duck classes!

And we can add new behaviors without modifying any of our existing behavior classes or
touching any of the Duck classes that use flying behavior.

## The Strategy Pattern

**It defines a family of algorithms, encapsulates ech one, and makes them interchangeable.
Strategy lets the algorithm vary independently from client that use it.**

References:

- Head First Design Patterns
