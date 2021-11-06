---
title: "[Dynamic Programming] Memoization & Tabulation Recipe"
published: true
tags: Algorithm
---

## Memoization

1. Make it work
   1. visualize the problem as a tree
   2. implement the tree using recursion
   3. test it
2. Make it efficient
   1. add a memo object
   2. add a base case to return memo values
   3. store return values into the memo

## Tabulation

1. visualize the problem as a table
2. size the table based on the inputs
3. initialize the table with default value
4. seed the trivial answer into the table
5. iterate through the table
6. fill further position based on the current position

## Reference

- [https://www.youtube.com/watch?v=oBt53YbR9Kk](https://www.youtube.com/watch?v=oBt53YbR9Kk)