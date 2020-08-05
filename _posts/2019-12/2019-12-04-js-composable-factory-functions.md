---
title: "JavaScript Composable Factory Functions"
published: true
tags: Node.js
---

Composable factory functions represents a particular type of factory function
that can be "composed" together to build new enhanced functions. They
are especially useful for allowing us to construct objects that "inherit"
behaviors and properties from different sources without the need for building
complex class hierarchies.

Let's assume we want to build a video game in which the characters on the screen
can have a number of different behaviors: they can *move* on the screen; they
can *slash* and *shoot*. And yes, to be a character they should have some basic
properties such as life points, position on the screen, and name.

We want to define several types of character, one for every specific behavior:

- **Character**: base character that has life points, a position and a name
- **Mover**: character that is able to move
- **Slasher**: character that is able to slash
- **Shooter**: character that is able to shoot (as long as it has bullets!)

Ideally we would be able to define new types of characters, combining different
behaviors from the existing ones, We want absolute freedom and, for example, we
would like to define these new types on top of the existing ones:

- **Runner**: a character that can move
- **Samurai**: a character that can move and slash
- **Sniper**: a character that can shoot (it doesn't move)
- **Gunslinger**: a character that can move and shoot
- **Western Samurai**: a character that can move, slash, and shoot

As you can see, we want total freedom in combining the features of every basic
type, so it should be obvious that we cannot easily model this problem using
classes and inheritance.

```javascript
const stampit = require('stampit')

const character = stampit().props({
    name: 'anonymous',
    lifePoints: 100,
    x: 0,
    y: 0
})

const c = character();
c.name = 'John'
c.lifePoints = 10;
```

```javascript
const mover = stampit().methods({
    move(xIncr, yIncr) {
        this.x += xIncr
        this.y += xIncr
        console.log(`${this.name} moved to [${this.x}, ${this.y}]`)
    }
})
```

```javascript
const slasher = stampit().methods({
    slash(direction){
        console.log(`${this.name} slashed to the ${direction}`)
    }
})
```

```javascript
const shooter = stampit().props({bullets: 6}).methods({
    shoot(direction){
        if(this.bullets > 0){
            --this.bullets;
            console.log(`${this.name} shoot to the ${direction}`)
        }
    }
})
```

```javascript
const runner = stampit.compose(character, mover)
const samurai = stampit.compose(character, mover, slasher)
const sniper = stampit.compose(character, shooter)
const gunslinger = stampit.compose(character, mover, shooter)
const westernSamurai = stampit.compose(gunslinger, samurai)
```

```javascript
const gojiro = westernSamurai()
gojiro.name = 'Gojiro Kiryu'
gojiro.slash('left')
gojiro.shoot('right')
```

## References

- Node.js Design Patterns
