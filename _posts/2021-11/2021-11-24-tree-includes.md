---
title: "[Tree] Tree Includes"
published: true
tags: Tree
---

## Problem

Write a function, treeIncludes, that takes in the root of a binary tree and a target value. The function should
return a boolean indicating whether or not the value is contained in the tree.

## DFS Recursion, DFS Stack, BFS Queue

```javascript
class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const treeIncludes = (root, target) => {
	// base case
	if(root === null) return false;
	if(root.val === target) return true

	return treeIncludes(root.left, target) || treeIncludes(root.right, target)
};

const treeIncludesStack = (root, target) => {
	if(root === null) return false;

	const stack = [root]

	while(stack.length > 0) {
		const current = stack.pop()
		if(current.val === target) return true;

		if(current.left) stack.push(current.left)
		if(current.right) stack.push(current.right)
	}

	return false;
}

const treeIncludesQueue = (root, target) => {
	if(root === null) return false;

	const queue = [root]

	while(queue.length > 0) {
		const current = queue.shift()
		if(current.val === target) return true;

		if(current.left) queue.push(current.left)
		if(current.right) queue.push(current.right)
	}

	return false;
}

{
	const a = new Node("a");
	const b = new Node("b");
	const c = new Node("c");
	const d = new Node("d");
	const e = new Node("e");
	const f = new Node("f");

	a.left = b;
	a.right = c;
	b.left = d;
	b.right = e;
	c.right = f;

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f

	console.log(
	treeIncludes(a, "e")); // -> true
	console.log(
		treeIncludesStack(a, "e")); // -> true
	console.log(
		treeIncludesQueue(a, "e")); // -> true
}

{
	const a = new Node("a");
	const b = new Node("b");
	const c = new Node("c");
	const d = new Node("d");
	const e = new Node("e");
	const f = new Node("f");

	a.left = b;
	a.right = c;
	b.left = d;
	b.right = e;
	c.right = f;

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f

	console.log(
	treeIncludes(a, "a")); // -> true
	console.log(
		treeIncludesStack(a, "a")); // -> true
	console.log(
		treeIncludesQueue(a, "a")); // -> true
}

{
	const a = new Node("a");
	const b = new Node("b");
	const c = new Node("c");
	const d = new Node("d");
	const e = new Node("e");
	const f = new Node("f");

	a.left = b;
	a.right = c;
	b.left = d;
	b.right = e;
	c.right = f;

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f

	console.log(
	treeIncludes(a, "n")); // -> false
	console.log(
		treeIncludesStack(a, "n")); // -> false
	console.log(
		treeIncludesQueue(a, "n")); // -> false
}

{
	const a = new Node("a");
	const b = new Node("b");
	const c = new Node("c");
	const d = new Node("d");
	const e = new Node("e");
	const f = new Node("f");
	const g = new Node("g");
	const h = new Node("h");

	a.left = b;
	a.right = c;
	b.left = d;
	b.right = e;
	c.right = f;
	e.left = g;
	f.right = h;

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h

	console.log(
	treeIncludes(a, "f")); // -> true
	console.log(
		treeIncludesStack(a, "f")); // -> true
	console.log(
		treeIncludesQueue(a, "f")); // -> true
}

{
	const a = new Node("a");
	const b = new Node("b");
	const c = new Node("c");
	const d = new Node("d");
	const e = new Node("e");
	const f = new Node("f");
	const g = new Node("g");
	const h = new Node("h");

	a.left = b;
	a.right = c;
	b.left = d;
	b.right = e;
	c.right = f;
	e.left = g;
	f.right = h;

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h

	console.log(
	treeIncludes(a, "p")); // -> false
	console.log(
		treeIncludesStack(a, "p")); // -> false
	console.log(
		treeIncludesQueue(a, "p")); // -> false
}

{
	console.log(
	treeIncludes(null, "b")); // -> false
	console.log(
		treeIncludesStack(null, "b")); // -> false
	console.log(
		treeIncludesQueue(null, "b")); // -> false
}
```

## Reference

- [https://www.youtube.com/watch?v=fAAZixBzIAI](https://www.youtube.com/watch?v=fAAZixBzIAI)