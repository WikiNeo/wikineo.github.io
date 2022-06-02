---
title: '[LeetCode 236] Lowest Common Ancestor of a Binary Tree'
published: true
tags: BinaryTree
---

## Problem

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes p and q as the lowest node in T that has both p
and q as descendants (where we allow **a node to be a descendant of itself**).”

### Example 1:

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

### Example 2:

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

### Example 3:

```
Input: root = [1,2], p = 1, q = 2
Output: 1
```
 
#### Constraints:

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the tree.

## Thoughts

- The node where it splits is the LCA
- DFS left, right

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

function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
    const dfs = (node: TreeNode): TreeNode => {
        if(node === null) {
            return null;
        }
        // descendant of itself
        if(node === p || node === q){
            return node;
        }
        
        const left: TreeNode = dfs(node.left);
        const right: TreeNode = dfs(node.right);
        
        // split
        if(left && right){
            return node;
        }
        // can't find
        if(!left && !right){
            return null
        }
        
        return left ? left : right;
    }
    
    return dfs(root)
};
```

## Reference

- [https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)