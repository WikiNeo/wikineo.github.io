---
title: 'TypeScript Notes'
published: true
tags: Node.js
---

## Project

### Init

```shell
yarn init
yarn add -D typescript
yarn run tsc --init
```

### Dev Server

```shell
yarn add -D ts-node-dev
"scripts": {
	"dev": "ts-node-dev --respawn --transpile-only index.ts"
},
yarn run dev
```

### ESlint

```shell
yarn add eslint --dev
yarn create @eslint/config
yarn add -D eslint-config-standard
yarn add -D @typescript-eslint/eslint-plugin
"source": true
yarn add -D @typescript-eslint/parser
yarn add -D eslint-plugin-import
yarn add -D eslint-plugin-node
yarn add -D eslint-plugin-promise
```
## Array

```TypeScript
let cats: string[] = ['Bob', 'Willy', 'Mini']

// add to end
cats.push('cat')

// remove from the end
let cat: string = cats.pop()

// remove from beginning
let cat: string = cats.shift()

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
let h: {[index: string]: number} = {a: 1, b: 2}

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

## Math

```TypeScript
Infinity
```

## Types

```TypeScript
boolean
```