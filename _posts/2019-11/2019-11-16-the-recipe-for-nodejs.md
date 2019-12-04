---
title: "The Recipe for Node.js"
published: true
---

The reactor pattern and libuv and the basic building blocks of Node.js but we
need the following three other components to build the full platform:

- A set of bindings responsible for wrapping and exposing libuv and other
  low-level functionality to JavaScript.
- **V8**, the JavaScript engine originally developed by Google for the Chrome
  browser. This is one of the reasons why Node.js is so fast and efficient. V8
  is acclaimed for its revolutionary design, its speed, and for its efficient
  memory management.
- A core JavaScript library (called **node-core**) that implements the
  high-level Node.js API

The following image represents Node.js final architecture:

![Node.js Architecture](/../../assets/Node.js-Architecture.png)

References:

- Node.js Design Patterns
