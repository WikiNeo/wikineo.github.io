---
title: "[Tree] Max Root to Leaf Sum"
published: true
tags: Tree
---

## Problem

Write a function, maxPathSum, that takes in the root of a binary tree that contains number values.
The function should return the maximum sum of any root to leaf path within the tree.

You may assume that the input tree is non-empty.

## Thoughts

1. Use DFS for this
2. For each node, return the sum of current node and its max left/right node
3. base case return 0.

## DFS Recursion

```javascript
class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const maxPathSum = (root) => {
	if(root === null) return -Infinity;
	if(root.left === null && root.right === null) return root.val
	const childSum = Math.max(maxPathSum(root.left), maxPathSum(root.right))

	return root.val + childSum;
};


{
	const a = new Node(3);
	const b = new Node(11);
	const c = new Node(4);
	const d = new Node(4);
	const e = new Node(-2);
	const f = new Node(1);

	a.left = b;
	a.right = c;
	b.left = d;
	b.right = e;
	c.right = f;

//       3
//    /    \
//   11     4
//  / \      \
// 4   -2     1

	console.log(
	maxPathSum(a)); // -> 18
}

{
	const a = new Node(5);
	const b = new Node(11);
	const c = new Node(54);
	const d = new Node(20);
	const e = new Node(15);
	const f = new Node(1);
	const g = new Node(3);

	a.left = b;
	a.right = c;
	b.left = d;
	b.right = e;
	e.left = f;
	e.right = g;

//        5
//     /    \
//    11    54
//  /   \
// 20   15
//      / \
//     1  3

	console.log(
	maxPathSum(a)); // -> 59
}

{
	const a = new Node(-1);
	const b = new Node(-6);
	const c = new Node(-5);
	const d = new Node(-3);
	const e = new Node(0);
	const f = new Node(-13);
	const g = new Node(-1);
	const h = new Node(-2);

	a.left = b;
	a.right = c;
	b.left = d;
	b.right = e;
	c.right = f;
	e.left = g;
	f.right = h;

//        -1
//      /   \
//    -6    -5
//   /  \     \
// -3   0    -13
//     /       \
//    -1       -2

	console.log(
	maxPathSum(a)); // -> -8
}

{
	const a = new Node(42);

//        42

	console.log(
	maxPathSum(a)); // -> 42
}
```

## Reference

- [https://www.youtube.com/watch?v=fAAZixBzIAI](https://www.youtube.com/watch?v=fAAZixBzIAI)