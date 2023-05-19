---
title: "Function.prototype.call()"
published: true
tags: Node.js
---

The `call()` method calls the function with a given `this` value and arguments provided individually.

```javascript
function Product(name, price) {
  this.name = name;
  this.price = price;
}

function Food(name, price) {
  Product.call(this, name, price);
  this.category = 'food';
}

console.log(new Food('cheese', 5).name);
// Expected output: "cheese"
```

## Syntax

```javascript
call(thisArg)
call(thisArg, arg1)
call(thisArg, arg1, /* …, */ argN)
```

## Parameters

### thisArg

- The value to use as `this` when calling `func`. If the function is not in `strict`
mode, `null` and `undefined` will be replaced with the global object, and
primitive values will be converted to objects.

### arg1, …, argN Optional

- Arguments for the function.

## Return value

The result of calling the function with the specified `this` value and arguments.

## Reference

- [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)