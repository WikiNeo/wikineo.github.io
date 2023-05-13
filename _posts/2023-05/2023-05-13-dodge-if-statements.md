---
title: "Dodge: 'if' statements"
published: true
tags: DesignPattern
---


```python
# Each new feature as an “if” statement.

class Logger:
    def __init__(self, pattern=None, file=None, sock=None, priority=None):
        self.pattern = pattern
        self.file = file
        self.sock = sock
        self.priority = priority

    def log(self, message):
        if self.pattern is not None:
            if self.pattern not in message:
                return
        if self.file is not None:
            self.file.write(message + '\n')
            self.file.flush()
        if self.sock is not None:
            self.sock.sendall((message + '\n').encode('ascii'))
        if self.priority is not None:
            syslog.syslog(self.priority, message)

# Works just fine.

logger = Logger(pattern='Error', file=sys.stdout)

logger.log('Warning: not that important')
logger.log('Error: this is important')
```

You may recognize this example as more typical of the Python design practices
you’ve encountered in real applications.

The `if` statement approach is not entirely without benefit. This class’s whole
range of possible behaviors can be grasped in a single reading of the code
from top to bottom. The parameter list might look verbose but, thanks to
Python’s optional keyword arguments, most calls to the class won’t need to
provide all four arguments.

(It’s true that this class can handle only one file and one socket, but that’s
an incidental simplification for the sake of readability. We could easily
pivot the `file` and `socket` parameters to lists named `files` and `sockets`.)

Given that every Python programmer learns `if` quickly, but can take much longer
to understand classes, it might seem a clear win for code to rely on the
simplest possible mechanism that will get a feature working. But let’s balance
that temptation by making explicit what’s been lost by dodging Composition
Over Inheritance:

1. **Locality.** Reorganizing the code to use `if` statements hasn’t been an
unmitigated win for readability. If you are tasked with improving or debugging
one particular feature — say, the support for writing to a socket — you will
find that you can’t read its code all in one place. The code behind that
single feature is scattered between the initializer’s parameter list, the
initializer’s code, and the `log()` method itself.

2. **Deletability.** An underappreciated property of good design is that it makes
deleting features easy. Perhaps only veterans of large and mature Python
applications will strongly enough appreciate the importance of code deletion
to a project’s health. In the case of our class-based solutions, we can
trivially delete a feature like logging to a socket by removing the
`SocketHandler` class and its unit tests once the application no longer needs
it. By contrast, deleting the socket feature from the forest of if statements
not only requires caution to avoid breaking adjacent code, but raises the
awkward question of what to do with the `socket` parameter in the initializer.
Can it be removed? Not if we need to keep the list of positional parameters
consistent — we would need to retain the parameter, but raise an exception if
it’s ever used.

3. **Dead code analysis.** Related to the previous point is the fact that when we
use Composition Over Inheritance, dead code analyzers can trivially detect
when the last use of `SocketHandler` in the codebase disappears. But dead code
analysis is often helpless to make a determination like “you can now remove
all the attributes and if statements related to socket output, because no
surviving call to the initializer passes anything for `socket` other than `None`.”

4. **Testing.** One of the strongest signals about code health that our tests provide
is how many lines of irrelevant code have to run before reaching the line
under test. Testing a feature like logging to a socket is easy if the test can
simply spin up a `SocketHandler` instance, pass it a live socket, and ask it to
`emit()` a message. No code runs except code relevant to the feature. But
testing socket logging in our forest of `if` statements will run at least three
times the number of lines of code. Having to set up a logger with the right
combination of several features merely to test one of them is an important
warning sign, that might seem trivial in this small example but becomes
crucial as a system grows larger.

5. **Efficiency.** I’m deliberately putting this point last, because readability and
maintainability are generally more important concerns. But the design problems
with the forest of `if` statements are also signalled by the approach’s
inefficiency. Even if you want a simple unfiltered log to a single file, every
single message will be forced to run an `if` statement against every possible
feature you could have enabled. The technique of composition, by contrast,
only runs code for the features you’ve composed together.

For all of these reasons, I suggest that the apparent simplicity of the if
statement forest is, from the point of view of software design, largely an
illusion. The ability to read the logger top-to-bottom as a single piece of
code comes at the cost of several other kinds of conceptual expense that will
grow sharply with the size of the codebase.

## Reference

- [https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-if-statements](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-if-statements)