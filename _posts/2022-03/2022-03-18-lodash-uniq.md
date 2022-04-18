---
title: 'Lodash uniq'
published: true
tags: Lodash
---

```typescript
_.uniq(array)
```

Creates a duplicate-free version of an array, using `SameValueZero` for equality
comparisons, in which only the first occurrence of each element is kept. The
order of result values is determined by the order they occur in the array.

## Since

- 0.1.0

## Arguments

- `array (Array)`: The array to inspect.

## Returns

- `(Array)`: Returns the new duplicate free array.

## Example

```typescript
_.uniq([2, 1, 2]);
// => [2, 1]
```

## Reference

- [https://lodash.com/docs/4.17.15#uniq](https://lodash.com/docs/4.17.15#uniq)