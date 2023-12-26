---
title: "Property 'private' in package.json"
published: true
tags: Node.js
---

## private

If you set `"private": true`` in your package.json, then npm will refuse to
publish it.

This is a way to prevent accidental publication of private repositories. If
you would like to ensure that a given package is only ever published to a
specific registry (for example, an internal registry), then use the
`publishConfig` dictionary described below to override the `registry` config param
at publish-time.

## Reference

- [https://docs.npmjs.com/cli/v7/configuring-npm/package-json#private](https://docs.npmjs.com/cli/v7/configuring-npm/package-json#private)