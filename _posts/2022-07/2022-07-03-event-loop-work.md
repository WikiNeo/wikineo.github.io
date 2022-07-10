---
title: 'How the Event Loop Works in Node.js'
published: true
tags: Node.js
---

## The Event Loop in Node.js

The Event Loop is composed of six phases, which are repeated for as long as
the application still has the code that needs to be executed:

1. Timers
2. I/O Callbacks
3. Waiting/Preparation
4. I/O Polling
5. `setImmediate`callbacks
6. Close events

The Event Loop starts at the moment Node.js begins to execute your `index.js` file, or any other application entry point.

These six phases create one cycle, or loop, which is known as a `tick`. A
Node.js process exits when there is no more pending work in the Event Loop, or
when `process.exit()` is called manually. A program only runs for as long as
there are tasks queued in the Event Loop, or present on the call stack.

Some phases are executed by the Event Loop itself, but for some of them the
main tasks are passed to the asynchronous C++ APIs.

### Phase 1: timers

The timers phase is executed directly by the Event Loop. At the beginning of
this phase the Event Loop updates its own time. Then it checks a queue, or
pool, of timers. This queue consists of all timers that are currently set. The
Event Loop takes the timer with the shortest wait time and compares it with
the Event Loop's current time. If the wait time has elapsed, then the timer's
callback is queued to be called once the call stack is empty.

The nature of executing timer callbacks as part of the Event Loop explains the
non-obvious feature that a timer's wait time is not an exact time in which the
callback will be executed -- it is, in fact, a minimum time that will pass
before the callback is queued for execution.

### Phase 2: I/O callbacks

This is a phase of non-blocking input/output.

This is what non-blocking I/O interfaces allow us to do. The asynchronous I/O request is recorded into the queue and then the main call stack can continue working as expected. In the second phase of the Event Loop the I/O callbacks of completed or errored out I/O operations are processed.

```javascript
fs.readFile("/file.md", (err, data) => {
  if (err) throw err;
});

myAwesomeFunction();
```

The `fs.readFile` operation is a classic I/O operation. Node.js will pass the
request to read a file filesystem of your OS. Then the code execution will
immediately continue past the `fs.readFile()` code to `myAwesomeFunction()`. When
the I/O operation is complete, or errors out, its callback will be placed in
the pending queue and it will be processed during the I/O callbacks phase of
the Event Loop.

### Phase 3: idle / waiting / preparation
This is a housekeeping phase. During this phase the Event Loop performs
internal operations of any callbacks. Technically speaking, there is no
possible direct influence on this phase, or its length. No mechanism is
present that could guarantee code execution during this phase. It is primarily
used for gathering information, and planning of what needs to be executed
during the next tick of the Event Loop.

### Phase 4: I/O polling (poll phase)

This is the phase in which all the JavaScript code that we write is executed, starting at the beginning of the file, and working down. Depending on the code it may execute immediately, or it may add something to the queue to be executed during a future tick of the Event Loop.

During this phase the Event Loop is managing the I/O workload, calling the functions in the queue until the queue is empty, and calculating how long it should wait until moving to the next phase. All callbacks in this phase are called synchronously in the order that they were added to the queue, from oldest to newest.

This is the phase that can potentially block our application if any of these callbacks are slow and not executed asynchronously.

Note: this phase is optional. It may not happen on every tick, depending on the state of your application.

If there are any `setImmediate()` timers scheduled, Node.js will skip this phase
during the current tick and move to the `setImmediate()` phase. If there are no
functions in the queue, and no timers, the application will wait for callbacks
to be added to the queue and execute them immediately, until the internal
`setTimeout()` that is set at the beginning of this phase is up. At that point,
it moves on to the next phase. The value of the delay in this timeout also
depends on the state of the application.

### Phase 5: setImmediate() callbacks

Node.js has a special timer, `setImmediate()`, and its callbacks are executed
during this phase. This phase runs as soon as the poll phase becomes idle. If
`setImmediate()` is scheduled within the I/O cycle it will always be executed
before other timers regardless of how many timers are present.

### Phase 6: close events

This phase executes the callbacks of all `close` events. For example, a close
event of web socket callback, or when `process.exit()` is called. This is when
the Event Loop is wrapping up one cycle and is ready to move to the next one.
It is primarily used to clean the state of the application.


## Summary

To summarize, one tick of the operation cycle of a Node.js application starts
with timers. Callbacks of timers for which the wait time is up are executed in
order from smallest wait time to largest. After that, I/O callbacks are
executed, followed by some internal processing. Then, it is time for the main
code to get into the picture and I/O poll queue callbacks are executed. Next,
callbacks of `setImmediate()` and close event callbacks are called. The next
tick starts with the timers. This cycle repeats as long as there is code that
needs to be executed.

## Reference

- [https://heynode.com/tutorial/how-event-loop-works-nodejs/](https://heynode.com/tutorial/how-event-loop-works-nodejs/)