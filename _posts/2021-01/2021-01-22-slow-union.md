---
title: 'Slow Union Query - MySQL'
published: true
tags: MySQL
---

## problem

```SQL
query1

UNION

query
```

query1 and query2 are fast queries, but the `UNION` one is slow

## explanation

A `UNION` (which is the same as `UNION DISTINCT`) or a `UNION ALL` causes a
temporary table to be created. For `UNION`, the table is created with an index
so that duplicates can be removed. With `UNION ALL`, there is no index.

## reference

- [Slow Union Query - MySQL](https://stackoverflow.com/questions/3524654/slow-union-query-mysql)