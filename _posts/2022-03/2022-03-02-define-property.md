---
title: 'Object.defineProperty()'
published: true
tags: Node.js
---

The static method `Object.defineProperty()` defines a new property directly on
an object, or modifies an existing property on an object, and returns the
object.

```TypeScript
const object1 = {};

Object.defineProperty(object1, 'property1', {
  value: 42,
  writable: false
});

object1.property1 = 77;
// throws an error in strict mode

console.log(object1.property1);
// expected output: 42
```

## Syntax

```TypeScript
Object.defineProperty(obj, prop, descriptor)
```

## Parameters

- `Object`
  - The object on which to define the property.
- `prop`
  - The name or `Symbol` of the property to be defined or modified.
- `descriptor`
  - The descriptor for the property being defined or modified

## Return Value

The object that was passed to the function.

## Reference

- [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)