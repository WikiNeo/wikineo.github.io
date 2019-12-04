---
title: "JavaScript Revealing Constructor"
published: true
---

```javascript
const promise = new Promise(function(resolve, reject) {
    // ...
})
```

`Promise` accepts a function as a constructor argument, which is called the
**executor function**. This function is called by the internal implementation of
the `Promise` constructor and it is used to allow the constructing code to
manipulate only a limited part of the internal state of the promise under
construction. In other words, it serves as a mechanism to expose the `resolve`
and `reject` functions so that they can be invoked to change the internal state
of the object.

The advantage of this is that only the constructing code has access to `resolve`
and `reject` and once the `promise` object is constructed, it can be passed
around safely; no other code will be able to call `reject` or `resolve` and
change the internal state of the promise.

## A read-only event emitter

Read-only event emitter is a special kind of event emitter which is not possible
to call the `emit` method (apart from within the function passed to the
constructor)

```javascript
const EventEmitter = require('events');

module.exports = class Roee extends EventEmitter {
    constructor(executor){
        super()
        const emit = this.emit.bind(this);
        this.emit = undefined;
        executor(emit);
    }
}
```

```javascript
const Roee = require('./roee')

const ticker = new Roee(emit => {
    let tickCount = 0;
    setInterval(() => emit('tick', tickCount++), 1000)
})

module.exports = ticker
```

```javascript
const ticker = require('./ticker')

ticker.on('tick', tickCount => console.log(tickCount, 'TICK'));
ticker.emit('something', {}); // this will fail
```

## References

- Node.js Design Patterns
