---
title: 'ESLint with Yarn for TypeScript project'
published: true
tags: Node.js
---

ESlint init only uses `npm` to install the dependencies, to use yarn, do
following

```shell
yarn add eslint --dev
yarn create @eslint/config

yarn add -D eslint-config-standard
yarn add -D @typescript-eslint/eslint-plugin
yarn add -D @typescript-eslint/parser
yarn add -D eslint-plugin-import
yarn add -D eslint-plugin-node
yarn add -D eslint-plugin-promise
```
