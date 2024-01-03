---
title: "Mocha with TypeScript"
published: true
tags: Node.js
---

You can use `ts-mocha`

```shell
ts-mocha
```

To add coverage

```shell
nyc ts-mocha
```

Or you can use

```shell
mocha --require ts-node/register

# or ths following for a significantly faster experience, as this avoids the Typescript type checking

mocha -require ts-node/register/transpile-only 
```
