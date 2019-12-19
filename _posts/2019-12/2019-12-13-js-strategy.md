---
title: "JavaScript Strategy"
published: false
---

The Strategy pattern enables an object, called the *Context*, to support
variation in its logic by extracting the *variable* parts into separate,
interchangeable objects called *Strategies*. The context implements the common
logic of a family of algorithms, while a strategy implements the mutable parts,
allowing the context to adapt its behavior depending on different factors such
as an input value, a system configuration, or user preferences. The strategies
are usually part of a family of solutions and all of them implement the same
interface, which is the one that is expected by the context.

We quickly understand how powerful this pattern is; not only does it help with
separating the concerns within an algorithm, but it also enables it to have
better flexibility and adapt to different variations of the same problem.

The Strategy pattern is particularly useful in all those situations where
supporting variations of an algorithm requires complex condition logic, or
mixing together different algorithms of the same family.

## Multi-format configuration objects



## References

- Node.js Design Patterns
