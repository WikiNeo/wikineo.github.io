---
title: 'ts-node-dev'
published: true
tags: Node.js
---

Tweaked version of node-dev that uses ts-node under the hood.

It restarts target node process when any of required files changes (as
standard `node-dev`) but shares Typescript compilation process between restarts.
This significantly increases speed of restarting comparing to `node-dev -r
ts-node/register ...`, `nodemon -x ts-node ...` variations because there is no
need to instantiate `ts-node` compilation each time.

## Usage

So you just combine `node-dev` and `ts-node` options (see docs of those packages):

```shell
tsnd --respawn server.ts
```

## Options

- `--exit-child` - Adds `'SIGTERM'` exit handler in a child process.

## Reference

- [https://www.npmjs.com/package/ts-node-dev](https://www.npmjs.com/package/ts-node-dev)
