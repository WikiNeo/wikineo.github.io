---
title: '[LeetCode 98] Validate Binary Search Tree'
published: true
tags: BinaryTree
---

## Problem

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A **valid BST** is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.
 
### Example 1:

```
Input: root = [2,1,3]
Output: true
```

### Example 2:

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

#### Constraints:

```
- The number of nodes in the tree is in the range [1, 104].
- -231 <= Node.val <= 231 - 1
```

## Thoughts

- Each node should satisfy its left & right boundary

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

function isValidBST(root: TreeNode | null): boolean {
    
    // each node should satisfy left & right boundary
    const valid = (node: TreeNode, left: number, right: number): boolean => {
        // base case
        if(node === null) {
            return true;
        }
        if(!(left < node.val && node.val < right)) {
            return false;
        }
        
        // recursive case
        return valid(node.left, left, node.val) && valid(node.right, node.val, right)
    }
    
    return valid(root, -Infinity, Infinity)
};
```

## Reference

- [https://leetcode.com/problems/validate-binary-search-tree/](https://leetcode.com/problems/validate-binary-search-tree/)