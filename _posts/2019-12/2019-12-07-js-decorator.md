---
title: "JavaScript Decorator"
published: true
tags: Node.js
---

Decorator is a structural pattern that consists of dynamically augmenting the
behavior of an existing object. It's different from classical inheritance,
because the behavior is not added to all the objects of the same class, but only
to the instances that are explicitly decorated.

Implementation-wise, it is very similar to the Proxy Pattern, but instead of
enhancing or modifying the behavior of the existing interface of an object, it
augments it with new functionalities.

The `Decorator` object is extending the `Component` object by adding the
`methodC()` operation. The existing methods are usually delegated to the
decorated object, without further processing. Of course,if necessary we can
easily combine the Proxy pattern so that the calls to the existing methods can
be intercepted and manipulated as well.

## Techniques for implementing Decorators

### Composition

Using composition, the decorated component is wrapped around a new object that
usually inherits from it. The Decorator in this case simply needs to define the
new methods, while delegating the existing ones to the original component

```javascript
function decorate(component){
    const proto = Object.getPrototypeOf(component)

    function Decorator(component){
        this.component = component
    }

    Decorator.prototype = Object.create(proto)

    // new method
    Decorator.prototype.greetings = function(){
        return 'Hi!'
    }

    // delegate method
    Decorator.prototype.hello = function(){
        return this.component.hello.apply(this.component, arguments)
    }

    return new Decorator(component)
}
```

### Object augmentation

Object decoration can also be achieved by simply attaching new methods directly
to the decorated object

```javascript
function decorate(component){
    // new method
    component.greetings = () => {
        // ...
    }
    return component
}
```

## Decorating a LevelUP database

### Implementing a LevelUP plugin

```javascript
module.exports = function levelSubscribe(db){
    db.subscribe = (pattern, listener) => {
        db.on('put', (key, val) => {
            const match = Object.keys(pattern).every(k => (pattern[k] === val[k]))
            if(match){
                listener(key, val)
            }
        })
    }
    return db;
}
```

```javascript
const level = require('level')
const levelSubscribe = require('./levelSubscribe')

let db = level(__dirname + '/db', {valueEncoding: 'json'})
db = levelSubscribe(db)

db.subscribe(
    {doctype: 'tweet', language: 'en'},
    (k, val) => console.log(val)
)
db.put('1', {doctype: 'tweet', text: 'Hi', language: 'en'})
db.put('2', {doctype: 'company', name: 'ACME Co.'})
```

## References

- Node.js Design Patterns
