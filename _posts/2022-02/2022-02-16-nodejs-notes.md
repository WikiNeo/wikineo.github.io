---
title: 'Node.js Notes'
published: true
tags: Node.js
---

## Array

```TypeScript
let cats: string[] = ['Bob', 'Willy', 'Mini']

// add to end
cats.push('cat')

// remove from the end
cats.pop()

// remove from beginning
cats.shift()

//add to beginning
cats.unshift('cat')

// loop 
for(let cat of cats){
	console.log(cat)
}

// clone
[...cats]
Array.from(cats)
```

## Hash

```TypeScript
let h: [{index: string}: number] = {a: 1, b: 2}

// value in hash
'a' in h

// number of keys
Object.keys(h).length

// loop
for(let key in h) {
	console.log(key)
	console.log(h[key])
}
```

## Set

```TypeScript
let s: Set<string> = new Set<string>()

s.add('s')
console.log(s.has('s'))
s.delete('s')
```