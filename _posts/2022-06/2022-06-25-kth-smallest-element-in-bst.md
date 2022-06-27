---
title: '[LeetCode 230] Kth Smallest Element in a BST'
published: true
tags: BinaryTree
---

## Problem

Given the `root` of a binary search tree, and an integer `k`, return the `kth` smallest value (**1-indexed**) of all the values of the nodes in the tree.

### Example 1:

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

### Example 2:

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```
 
### Constraints:

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4`

## Thoughts

- For a BST, inorder traversal is the sorted order.
- We can use a count to find the kth smallest element with inorder traversal

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

function kthSmallest(root: TreeNode | null, k: number): number {
    let res;
    
    const travel = (node: TreeNode) => {
        if(node === null) return
        if(k === 0) return
        
        travel(node.left)
        k--;
        if(k === 0) res = node.val;
        travel(node.right)
    }
    
    travel(root)
    
    return res
};
```

## Reference

- [https://leetcode.com/problems/kth-smallest-element-in-a-bst/](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)