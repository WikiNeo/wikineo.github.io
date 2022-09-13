---
title: 'Python Scopes and Namespaces Example'
published: true
tags: Python
---

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

Output

```shell
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

Note how the *local* assignment (which is default) didn’t change *scope_test*'s
binding of *spam*. The nonlocal assignment changed *scope_test*'s binding of *spam*,
and the global assignment changed the module-level binding.

## Reference

- [https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example](https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example)