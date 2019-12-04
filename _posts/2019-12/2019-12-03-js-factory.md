---
title: "JavaScript Factory Design Pattern"
published: true
---

## A generic interface for creating objects

In JavaScript, the functional paradigm is often preferred to a purely
object-oriented design, for its simplicity, usability, and small surface area.
Invoking a factory, instead of directly creating a new object from a prototype
using the `new` operator or `Object.create()`, is so much more convenient and
flexible in several respects.

First and foremost, a factory allows us to separate the object creation from its
implementation; essentially, a factory wraps the creation of a new instance
giving us more flexibility and control in the way we do it. Inside the factory,
we can create a new instance leveraging closures, using a prototype and the
`new` operator, using `Object.create()`, or even returning a different instance
based on a particular condition. The consumer of the factory is totally agnostic
about how the creation of the instance is carried out. Ths truth is that, by
using `new`, we are binding our code to one specific way of creating an object,
while in JavaScript we can have much more flexibility, almost for free.

As a quick example, let's consider a simple factory that creates an `Image`
object:

```javascript
function createImage(name){
    return new Image(name);
}
const image = createImage('photo.jpg');
```

The `createImage()` factory might look totally unnecessary; why not instantiate
the `Image` class using the `new` operator directly?

```javascript
const image = new Image(name);
```

As we already mentioned, using `new` binds our code to one particular type of
object; in the preceding case, to objects of type `Image`. A factory gives us
much more flexibility; imagine that we want to refactor the `Image` class,
splitting it into smaller classes, one for each image format we support.

```javascript
function createImage(name){
    if(name.match(/\.jpeg$/)){
        return new JpegImage(name)
    } else if (name.match(/.gif$/)){
        return new GifImage(name)
    } else if (name.match(/.png$)){
        return new PngImage(name)
    } else {
        throw new Exception('Unsupported format')
    }
}
```

Our factory also allows us not expose the constructors of the object it creates,
and prevents them from being extended or modified. In Node.js, this can be
achieved by exploring only the factory, while keeping each constructor private.

### A mechanism to enforce encapsulation

A factory can also be used as an encapsulation mechanism, thanks to closures.

#### Encapsulation

Encapsulation refers to he technique of controlling the access to some internal
details of an object by preventing the external code from manipulating them
directly. The interaction with the object happens only through its public
interface, isolating the external code from the changes in the implementation
details of the object. This practice is also referred to as information hiding.
Encapsulation is also a fundamental principle of object-oriented design,
together with inheritance, polymorphism, and abstraction.

```javascript
function createPerson(name){
    const privateProperties = {}

    const person = {
        setName: name => {
            if(!name) throw new Error('A person must have a name');
            privateProperties.name = name;
        },
        getName: () => {
            return privateProperties.name
        }
    }

    person.setName(name)
    return person;
}
```

In the preceding code, we leverage closures to create two objects: a person
object which represents the public interface returned by the factory and a group
of `privateProperties` that are inaccessible from the outside and that can be
manipulated only through the interface provided by the `Person` object. For
example, in the preceding code, we make sure that a person's `name` is never
empty; this would not be possible to enforce if `name` was just a property of
the `person` object.

## Building a simple code profiler

Let's build a simple *code profiler*, an object with the following properties:

- A `start()` method that triggers the start of a profiling session
- An `end()` method to terminate the session and log its execution time to the console.

```javascript
class Profiler {
    constructor(label) {
        this.label = label;
        this.lastTime = null;
    }

    start(){
        this.lastTime = process.hrtime();
    }

    end(){
        const diff = process.hrtime(this.lastTime);
        console.log(`Timer "${this.label}" took ${diff[0]} seconds and ${diff[1]} nanoseconds.`)
    }
}
```

```javascript
module.exports = function(label){
    if(process.env.NODE_ENV === 'development'){
        return new Profiler(label)
    } else if (process.env.NODE_ENV === 'production') {
        return {
            start: function() {},
            end: function(){}
        }
    } else {
        throw new Error('Must set NODE_ENV')
    }
}
```

## References

- Node.js Design Patterns
