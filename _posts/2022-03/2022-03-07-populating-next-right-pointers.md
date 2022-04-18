---
title: '[LeetCode 116] Convert Sorted Array to Binary Search Tree'
published: true
tags: BinaryTree
---

## Problem

You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to `NULL`.

### Example 1:

```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

### Example 2:

```
Input: root = []
Output: []
```
 
#### Constraints:

```
- The number of nodes in the tree is in the range [0, 212 - 1].
- -1000 <= Node.val <= 1000
```
 
#### Follow-up:

```
- You may only use constant extra space.
- The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
```

## TypeScript

```typescript
/**
 * Definition for Node.
 * class Node {
 *     val: number
 *     left: Node | null
 *     right: Node | null
 *     next: Node | null
 *     constructor(val?: number, left?: Node, right?: Node, next?: Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function connect(root: Node | null): Node | null {
    // special case
    if(root === null) return null;
    
    const build = (cur: Node, parent: Node, isLeft: boolean): void => {
        // base case
        if(cur === null) {
            return;
        }
        
        // deal with left, right
        if(isLeft){
            cur.next = parent.right;
        } else {
            if(parent.next === null){
                cur.next = null
            } else {
                cur.next = parent.next.left;    
            }
        }
        
        // recursion call
        build(cur.left, cur, true);
        build(cur.right, cur, false);
    }
    
    // driver code
    root.next = null;
    build(root.left, root, true);
    build(root.right, root, false);
    
    return root;
};
```

## Reference

- [https://leetcode.com/problems/populating-next-right-pointers-in-each-node/](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)