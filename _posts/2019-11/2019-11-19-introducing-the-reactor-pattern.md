---
title: "Introducing the Reactor Pattern"
published: true
tags: DesignPattern
---

The main idea behind reactor pattern is to have a handler (which in Node.js is
represented by a *callback* function) associated with each I/O operation, which
will be invoked as soon as an event is produced and processed by the event loop.

![the reactor pattern](/../../assets/reactor-pattern.png)

This is what happens in an application using the reactor pattern:

1. The application generates a new I/O operation by submitting a request to the
   **Event Demultiplexer**. The application also specifies an handler, which
   will be invoked when the operation completes. Submitting a new requests to
   the **Event Demultiplexer** is a non-blocking call and it immediately returns
   control to the application.
2. When a set of I/O operations completes, the **Event Demultiplexer** pushes
   new events into **Event Queue**.
3. At this point, the **Event Loop** iterates over the items of the **Event Queue**.
4. For each event, the associated event handler is invoked.
5. The handler, which is part of the application code, will give back control to
   the **Event Loop** when its execution completes (5a). However, new
   asynchronous operations might be requested during the execution of the
   handler (5b), causing new operation to be inserted in the **Event
   Demultiplexer** (1), before control is given back to the **Event Loop**.
6. When all the items in the **Event Queue** are processed, the loop will block
   again on the **Event Demultiplexer** which will then trigger another cycle
   when a new event is available.

The asynchronous behavior is now clear: the application expresses the interest
to access a resource at one point in time (without blocking) and provides a
handler, which will then be invoked at another point in time when the operation
completes.

## Notes

A Node.js application will exit automatically when there are no more pending
operations in the Event Demultiplexer, and no more events to be processed inside
the **Event Queue**.

**Pattern (reactor)** handles I/O by blocking until new events are available
from a set of observed resources, and then reacts by dispatching each event to
an associated handler.

References:

- Node.js Design Patterns
