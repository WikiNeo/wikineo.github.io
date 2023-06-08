---
title: "Prim's Algorithm"
published: true
tags: Graph
---

In computer science, Prim's algorithm (also known as Jarník's algorithm) is a
greedy algorithm that finds a minimum spanning tree for a weighted undirected
graph. This means it finds a subset of the edges that forms a tree that
includes every vertex, where the total weight of all the edges in the tree is
minimized. The algorithm operates by building this tree one vertex at a time,
from an arbitrary starting vertex, at each step adding the cheapest possible
connection from the tree to another vertex.

## Description

The algorithm may informally be described as performing the following steps:

1. Initialize a tree with a single vertex, chosen arbitrarily from the graph.
2. Grow the tree by one edge: Of the edges that connect the tree to vertices not yet in the tree, find the minimum-weight edge, and transfer it to the tree.
3. Repeat step 2 (until all vertices are in the tree).

## Reference

- [https://en.wikipedia.org/wiki/Prim%27s_algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm)