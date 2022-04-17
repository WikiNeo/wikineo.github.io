---
title: '[Structural] Flyweight'
published: true
tags: DesignPattern
---

## Real world example

Did you ever have fresh tea from some stall? They often make more than one cup
that you demanded and save the rest for any other customer so to save the
resources e.g. gas etc. Flyweight pattern is all about that i.e. sharing.

## In plain words

It is used to minimize memory usage or computational expenses by sharing as
much as possible with similar objects.

## Wikipedia says

In computer programming, flyweight is a software design pattern. A flyweight
is an object that minimizes memory use by sharing as much data as possible
with other similar objects; it is a way to use objects in large numbers when a
simple repeated representation would use an unacceptable amount of memory.

## Programmatic example

Translating our tea example from above. First of all we have tea types and tea
maker

```typescript
// Anything that will be cached is fly weight
// Types of tea here will be flyweights
class KaraTea {

}

// acts as a factory and saves the tea
class TeaMaker {
    protected availableTea = [];

    make(preference) {
        if(!this.availableTea[preference]) {
            this.availableTea[preference] = new KaraTea()
        }
        return this.availableTea[preference]
    }
}
```

Then we have the `TeaShop` which takes orders and serves them

```typescript
class TeaShop {
    protected orders;
    protected teaMaker;

    constructor(teaMaker: TeaMaker) {
        this.teaMaker = teaMaker;
    }

    takeOrder(teaType: string, table: number){
        this.orders[table] = this.teaMaker.make(teaType)
    }

    serve(){
        this.orders.forEach((table, tea) => {
            console.log(`Serving team to table #{table}`)
        })
    }

}
```

And it can be used as below

```typescript
const teaMaker = new TeaMaker()
const shop = new TeaShop(teaMaker)

shop.takeOrder('less sugar', 1)
shop.takeOrder('more milk', 2)
shop.takeOrder('no sugar', 5)

shop.serve()
```

## References

- [https://github.com/kamranahmedse/design-patterns-for-humans](https://github.com/kamranahmedse/design-patterns-for-humans)
- [https://github.com/torokmark/design_patterns_in_typescript](https://github.com/torokmark/design_patterns_in_typescript)
- [https://refactoring.guru/design-patterns](https://refactoring.guru/design-patterns)