---
title:  "Binary Trees Terminology"
published: true
tags: Tree
---

- **leaves**: nodes with no children.
- **siblings**: nodes with the same parent.
- **depth of node**: number of edges from the root to the node
- **height of node**: number of edges from the node to the deepest leaf
- **height of tree**: height of the root
- **full binary tree**: a binary tree in which each node has exactly zero or two children
- **complete binary tree**: a binary tree which is completely filled, with the possible
  exception of the bottom level, which is filled from left to right.

References: [https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html)

## Leaf

A node with no children

## Node

### Depth of a node

The depth of a node is the number of edges from the node to the
tree's root node. A root node will have a depth of 0.

### Height of a node

The height of a node is the number of edges on the longest path from
the node to a leaf. A leaf node will have a height of 0.

## Tree

### Height of a tree

The height of a tree would be the height of its root node, or equivalently, the depth of its deepest node.

### Diameter (or width) of a tree

The diameter (or width) of a tree is the number of nodes on the longest path between any two leaf nodes.
