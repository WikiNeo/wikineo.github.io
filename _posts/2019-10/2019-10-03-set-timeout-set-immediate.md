---
title: "Node.js setTimeout vs setImmediate"
published: true
tags: Node.js
---

`setImmediate()` is equivalent to `setTimeout(fn, 0)`, but with some slight advantages.

`setTimeout(fn, delay)` calls the give callbacks after the given `delay` has ellapsed (in
milliseconds). However, the callback is not executed immediately at this time, but added
to the function queue so that it is executed **as soon as possible**, after all the
currently executing and currently queued event handlers have completed. Setting the delay
to 0 adds the callback to the queue immediately so that it is executed as soon as all
currently queued functions are finished.

`setImmediate` achieves the same effect, except that it doesn't use the queue of
functions. Instead, it checks the queue of I/O event handlers. If an I/O events in the
current snapshot are processed, it executes the callback. It queue them immediately after
the last I/O handler, somewhat like `process.nextTick`. This is faster than
`setTimeout(fn, 0)`.

## Code

```nodejs
console.log("first");
setTimeout(() => {
    console.log("second");
}, 0);
console.log("third");
```

```node.js
console.log("first");
setImmediate(() => {
    console.log("second");
});
console.log("third");
```

References:

- [https://www.toptal.com/nodejs/interview-questions](https://www.toptal.com/nodejs/interview-questions)
