---
title: "contextlib.suppress(*exceptions)"
published: true
tags: Python
---

Return a context manager that suppresses any of the specified exceptions if
they occur in the body of a with statement and then resumes execution with the
first statement following the end of the with statement.

As with any other mechanism that completely suppresses exceptions, this
context manager should be used only to cover very specific errors where
silently continuing with program execution is known to be the right thing to
do.

For example:

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('somefile.tmp')

with suppress(FileNotFoundError):
    os.remove('someotherfile.tmp')
```

This code is equivalent to:

```python
try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

try:
    os.remove('someotherfile.tmp')
except FileNotFoundError:
    pass
```

## Reference

- [https://docs.python.org/3/library/contextlib.html#contextlib.suppress](https://docs.python.org/3/library/contextlib.html#contextlib.suppress)
