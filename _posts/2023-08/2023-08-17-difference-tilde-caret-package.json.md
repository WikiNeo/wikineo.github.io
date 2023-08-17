---
title: "What's the difference between tilde(~) and caret(^) in package.json?"
published: true
tags: Node.js
---

- `~version` **“Approximately equivalent to version”**, will update you to all future patch versions, without incrementing the minor version. `~1.2.3` will use releases from `1.2.3` to `<1.3.0`.

- `^version` **“Compatible with version”**, will update you to all future minor/patch versions, without incrementing the major version. `^1.2.3` will use releases from `1.2.3` to `<2.0.0`.

## Reference

- [https://stackoverflow.com/questions/22343224/whats-the-difference-between-tilde-and-caret-in-package-json](https://stackoverflow.com/questions/22343224/whats-the-difference-between-tilde-and-caret-in-package-json)