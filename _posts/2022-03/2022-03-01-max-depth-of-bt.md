---
title: '[LeetCode 104] Maximum Depth of Binary Tree'
published: true
tags: BinaryTree
---

## Problem

Given the `root` of a binary tree, return its maximum depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Example 1:

```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

### Example 2:

```
Input: root = [1,null,2]
Output: 2
```
 
#### Constraints:

```
- The number of nodes in the tree is in the range [0, 104].
- -100 <= Node.val <= 100
```

## TypeScript

```typescript
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function maxDepth(root: TreeNode | null): number {
    
    const depth = (node: TreeNode): number => {
        if(node === null) return 0;
        
        const leftDepth: number = 1 + depth(node.left);
        const rightDepth: number = 1 + depth(node.right);
        
        return Math.max(leftDepth, rightDepth)
    }
    
    return depth(root);
};
```

## Reference

- [https://leetcode.com/problems/maximum-depth-of-binary-tree/](https://leetcode.com/problems/maximum-depth-of-binary-tree/)