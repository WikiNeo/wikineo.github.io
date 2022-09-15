---
title: 'Type Assertions'
published: true
tags: Node.js
---

Sometimes you will have information about the type of a value that TypeScript can’t know about.

For example, if you’re using `document.getElementById`, TypeScript only knows
that this will return some kind of `HTMLElement`, but you might know that your
page will always have an `HTMLCanvasElement` with a given ID.

In this situation, you can use a type assertion to specify a more specific
type:

```typescript
const myCanvas = document.getElementById("main_canvas") as HTMLCanvasElement;
```

Like a type annotation, type assertions are removed by the compiler and won’t affect the runtime behavior of your code.

You can also use the angle-bracket syntax (except if the code is in a `.tsx`
file), which is equivalent:

```typescript
const myCanvas = <HTMLCanvasElement>document.getElementById("main_canvas");
```

> Reminder: Because type assertions are removed at compile-time, there is no runtime checking associated with a type assertion. There won’t be an exception or null generated if the type assertion is wrong.

TypeScript only allows type assertions which convert to a more specific or less specific version of a type. This rule prevents “impossible” coercions like:

```typescript
const x = "hello" as number;
Conversion of type 'string' to type 'number' may be a mistake because neither type sufficiently overlaps with the other. If this was intentional, convert the expression to 'unknown' first.
```

Sometimes this rule can be too conservative and will disallow more complex
coercions that might be valid. If this happens, you can use two assertions,
first to `any` (or unknown), then to the desired type:

```typescript
const a = (expr as any) as T;
```

## Reference

- [https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions)