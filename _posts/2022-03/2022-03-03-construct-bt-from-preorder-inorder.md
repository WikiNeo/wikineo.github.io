---
title: '[LeetCode 105] Construct Binary Tree from Preorder and Inorder Traversal'
published: true
tags: BinaryTree
---

## Problem

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

### Example 1:

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

### Example 2:

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```
 
#### Constraints:

```
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.
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

function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
    // inorder
    const inorderValueToIndex: {[index: number]: number} = {}
    for(let i = 0; i < inorder.length; i++){
        inorderValueToIndex[inorder[i]] = i;
    }
    
    // preorder
    let preorderIndex: number = 0;
    
    // build tree with left, right in inorder array
    // & preorder index
    const build = (left: number, right: number): TreeNode => {
        // base case
        if(left > right) {
            return null;
        }
        
        // recursion case
        const rootValue: number = preorder[preorderIndex]
        const root: TreeNode = new TreeNode(rootValue);
        preorderIndex++;
        
        const mid: number = inorderValueToIndex[rootValue]
        
        root.left = build(left, mid - 1);
        root.right = build(mid + 1, right);
        
        return root;
    }
    
    return build(0, inorder.length - 1);
};
```

## Reference

- [https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)