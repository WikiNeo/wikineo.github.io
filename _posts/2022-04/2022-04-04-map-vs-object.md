---
title: 'Map vs Object in Javascript'
published: true
tags: Node.js
---

1. Keys. Object key is strings or symbols. Map keys can also be numbers (1 and
   "1" are different), objects, `NaN`, etc. It uses `===` to distinguish
   between keys, with one exception `NaN !== NaN` but you can use `NaN` as a
   key.

2. Order. The insertion order is remembered. So `[...map]` or
   `[...map.keys()]` has a particular order.

3. Interface. Object: `obj[key]` or `obj.a` (in some language, `[]` and `[]=` are
   really part of the interface). Map has `get()`, `set()`, `has()`, `delete()` etc.
   Note that you can use `map[123]`, but that is using it as a plain JavaScript
   object.

## Reference

- [https://stackoverflow.com/questions/18541940/map-vs-object-in-javascript](https://stackoverflow.com/questions/18541940/map-vs-object-in-javascript)