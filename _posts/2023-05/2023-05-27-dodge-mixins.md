---
title: "Dodge: 'Mixins' statements"
published: true
tags: DesignPattern
---

The `FilteredSocketLogger` in the previous section needed its own custom
`__init__()` method because it needed to accept arguments for both of its base
classes. But it turns out that this liability can be avoided. Of course, in
cases where a subclass doesn’t require any extra data, the problem doesn’t
arise. But even classes that do require extra data can have it delivered by
other means.

We can make the `FilteredLogger` more friendly to multiple inheritance if we
provide a default value for `pattern` in the class itself and then invite
callers to customize the attribute directly, out-of-band of initialization:

```python
# Don’t accept a “pattern” during initialization.

class FilteredLogger(Logger):
    pattern = ''

    def log(self, message):
        if self.pattern in message:
            super().log(message)

# Multiple inheritance is now simpler.

class FilteredSocketLogger(FilteredLogger, SocketLogger):
    pass  # This subclass needs no extra code!

# The caller can just set “pattern” directly.

logger = FilteredSocketLogger(sock1)
logger.pattern = 'Error'

# Works just fine.

logger.log('Warning: not that important')
logger.log('Error: this is important')

print('The socket received: %r' % sock2.recv(512))
```

```
The socket received: b'Error: this is important\n'
```

Having pivoted the `FilteredLogger` to an initialization maneuver that’s
orthogonal to that of its base class, why not push the idea of orthogonality
to its logical conclusion? We can convert the `FilteredLogger` to a “mixin” that
lives entirely outside the class hierarchy with which multiple inheritance
will combine it.

```python
# Simplify the filter by making it a mixin.

class FilterMixin:  # No base class!
    pattern = ''

    def log(self, message):
        if self.pattern in message:
            super().log(message)

# Multiple inheritance looks the same as above.

class FilteredLogger(FilterMixin, FileLogger):
    pass  # Again, the subclass needs no extra code.

# Works just fine.

logger = FilteredLogger(sys.stdout)
logger.pattern = 'Error'
logger.log('Warning: not that important')
logger.log('Error: this is important')
```

```
Error: this is important
```

The mixin is conceptually simpler than the filtered subclass we saw in the
last section: it has no base class that might complicate method resolution
order, so `super()` will always call the next base class listed in the `class`
statement.

A mixin also has a simpler testing story than the equivalent subclass. Whereas
the `FilteredLogger` would need tests that both run it standalone and also
combine it with other classes, the `FilterMixin` only needs tests that combine
it with a logger. Because the mixin is by itself incomplete, a test can’t even
be written that runs it standalone.

But all the other liabilities of multiple inheritance still apply. So while
the mixin pattern does improve the readability and conceptual simplicity of
multiple inheritance, it’s not a complete solution for its problems.

## Reference

- [https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-mixins](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-mixins)