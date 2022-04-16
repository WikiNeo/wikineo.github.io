---
title: '[Behavioral] Chain of Responsibility'
published: true
tags: DesignPattern
---

## Real world example

For example, you have three payment methods (`A`, `B` and `C`) setup in your account; each having a different amount in it.
`A` has 100 USD, `B` has 300 USD and C having `1000` USD and the preference for payments is chosen as `A` then `B` then `C`.
You try to purchase something that is worth 210 USD. Using Chain of Responsibility, first of all account `A` will be
checked if it can make the purchase, if yes purchase will be made and the chain will be broken. If not, request
will move forward to account `B` checking for amount if yes chain will be broken otherwise the request will keep
forwarding till it finds the suitable handler. Here `A`, `B` and `C` are links of the chain and the whole phenomenon is
Chain of Responsibility.

## In plain words

It helps building a chain of objects. Request enters from one end and keeps going from object to object till it
finds the suitable handler.

## Wikipedia says

In object-oriented design, the chain-of-responsibility pattern is a design pattern consisting of a source of
command objects and a series of processing objects. Each processing object contains logic that defines the types
of command objects that it can handle; the rest are passed to the next
processing object in the chain.

## Programmatic Example

First of all we have a base account having the logic for chaining the accounts
together and some accounts

```typescript
abstract class Account {
    protected successor: Account;
    protected balance: number;

    setNext(account: Account): void {
        this.successor = account;
    }

    canPay(amount): boolean {
        return this.balance >= amount;
    }

    getBalance(): number {
        return this.balance;
    }

    pay(amountToPay: number) : void{
        if(this.canPay(amountToPay)) {
            console.log(`Paid ${amountToPay} using ${this.constructor.name}`)
            this.balance -= amountToPay;
        } else if(this.successor) {
            console.log(`Cannot pay using ${this.constructor.name}, proceeding...`)
            this.successor.pay(amountToPay)
        } else {
            throw new Error('None of the accounts have enough balance')
        }
    }
}

class Bank extends Account {
    protected balance

    constructor(balance: number) {
        super()
        this.balance = balance;
    }
}

class Paypal extends Account {
    protected balance

    constructor(balance: number) {
        super()
        this.balance = balance;
    }
}

class Bitcoin extends Account {
    protected balance

    constructor(balance: number) {
        super()
        this.balance = balance;
    }
}
```

Now let's prepare the chain using the links defined above (i.e. Bank, Paypal,
Bitcoin)

```typescript
// Let's prepare a chain like below
//      $bank->$paypal->$bitcoin
//
// First priority bank
//      If bank can't pay then paypal
//      If paypal can't pay then bit coin
test('test chain-of-responsibility design patterns', () => {
    const bank = new Bank(100)
    const paypal = new Paypal(200)
    const bitcoin = new Bitcoin(300)
    bank.setNext(paypal)
    paypal.setNext(bitcoin)

    expect(bank.getBalance()).toEqual(100)
    expect(paypal.getBalance()).toEqual(200)
    expect(bitcoin.getBalance()).toEqual(300)

    // Let's try to pay using the first priority i.e. bank
    bank.pay(259)

    // Output will be
    // ==============
    // Cannot pay using bank. Proceeding ..
    // Cannot pay using paypal. Proceeding ..:
    // Paid 259 using Bitcoin!
    expect(bank.getBalance()).toEqual(100)
    expect(paypal.getBalance()).toEqual(200)
    expect(bitcoin.getBalance()).toEqual(41)
})
```

## References

- [https://github.com/kamranahmedse/design-patterns-for-humans](https://github.com/kamranahmedse/design-patterns-for-humans)
- [https://github.com/torokmark/design_patterns_in_typescript](https://github.com/torokmark/design_patterns_in_typescript)
- [https://refactoring.guru/design-patterns](https://refactoring.guru/design-patterns)