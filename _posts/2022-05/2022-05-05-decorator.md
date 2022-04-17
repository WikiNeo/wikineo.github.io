---
title: '[Structural] Decorator'
published: true
tags: DesignPattern
---

## Real world example

Imagine you run a car service shop offering multiple services. Now how do you
calculate the bill to be charged? You pick one service and dynamically keep
adding to it the prices for the provided services till you get the final cost.
Here each type of service is a decorator.

## In plain words

Decorator pattern lets you dynamically change the behavior of an object at run
time by wrapping them in an object of a decorator class.

## Wikipedia says

In object-oriented programming, the decorator pattern is a design pattern that
allows behavior to be added to an individual object, either statically or
dynamically, without affecting the behavior of other objects from the same
class. The decorator pattern is often useful for adhering to the Single
Responsibility Principle, as it allows functionality to be divided between
classes with unique areas of concern.

## Programmatic Example

Lets take coffee for example. First of all we have a simple coffee
implementing the coffee interface

```typescript
interface Coffee {
    getCost() : number;
    getDescription(): string;
}

class SimpleCoffee implements Coffee {
    getCost() {
        return 10;
    }

    getDescription() {
        return 'Simple coffee'
    }
}
```

We want to make the code extensible to allow options to modify it if required.
Lets make some add-ons (decorators)

```typescript
class MilkCoffee implements Coffee {
    protected coffee: Coffee;

    constructor(coffee: Coffee) {
        this.coffee = coffee;
    }

    getCost(): number {
        return this.coffee.getCost() + 2;
    }

    getDescription(): string {
        return this.coffee.getDescription() + ', milk'
    }
}

class WhipCoffee implements Coffee {
    protected coffee: Coffee;

    constructor(coffee: Coffee) {
        this.coffee = coffee;
    }

    getCost(): number {
        return this.coffee.getCost() + 5;
    }

    getDescription(): string {
        return this.coffee.getDescription() + ', whip'
    }
}

class VanillaCoffee implements Coffee {
    protected coffee: Coffee;

    constructor(coffee: Coffee) {
        this.coffee = coffee;
    }

    getCost(): number {
        return this.coffee.getCost() + 3;
    }

    getDescription(): string {
        return this.coffee.getDescription() + ', vanilla'
    }
}
```

Lets make a coffee now

```typescript
let coffee = new SimpleCoffee()
coffee.getCost()
coffee.getDescription()

coffee = new MilkCoffee(coffee)
coffee.getCost()
coffee.getDescription()

coffee = new WhipCoffee(coffee)
coffee.getCost()
coffee.getDescription()
```


## References

- [https://github.com/kamranahmedse/design-patterns-for-humans](https://github.com/kamranahmedse/design-patterns-for-humans)
- [https://github.com/torokmark/design_patterns_in_typescript](https://github.com/torokmark/design_patterns_in_typescript)
- [https://refactoring.guru/design-patterns](https://refactoring.guru/design-patterns)