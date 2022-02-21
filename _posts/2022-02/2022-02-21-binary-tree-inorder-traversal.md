---
title: '[LeetCode 94] Binary Tree Inorder Traversal'
published: true
tags: BinaryTree
---

## Problem

Given the `root` of a binary tree, return the inorder traversal of its nodes' values.

### Example 1:

```
Input: root = [1,null,2,3]
Output: [1,3,2]
```

### Example 2:

```
Input: root = []
Output: []
```

### Example 3:

```
Input: root = [1]
Output: [1]
```
 
### Constraints:

```
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
```

## TypeScript

```TypeScript
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

function inorderTraversal(root: TreeNode | null): number[] {
    const res: number[] = [];
    
    const run = (node: TreeNode): void => {
        if(node === null) return ;
        
        run(node.left)
        res.push(node.val)
        run(node.right)
    }
    
    run(root)
    return res;
};
```

## Reference

- [https://leetcode.com/problems/binary-tree-inorder-traversal/](https://leetcode.com/problems/binary-tree-inorder-traversal/)