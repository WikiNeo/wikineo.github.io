---
title: '[LeetCode 572] Subtree of Another Tree'
published: true
tags: BinaryTree
---

## Problem

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

### Example 1:

```
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

### Example 2:

```
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```
 
### Constraints:

- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
- `-10^4 <= root.val <= 10^4`
- `-10^4 <= subRoot.val <= 10^4`

## Thoughts

- For each node of the main tree, treat it as the root as the subtree, if the
  two subtrees are the same, returns true

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

function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
    
    const isIdentical = (node1: TreeNode, node2: TreeNode): boolean => {
        let identicalRes: boolean  = true;
        
        const travel = (node1: TreeNode, node2: TreeNode) => {
            if(identicalRes === false) return;
            if(node1 === null && node2 === null) return
            
            if(node1 === null || node2 === null || node1.val !== node2.val){
                identicalRes = false;
                return
            }
            travel(node1.left, node2.left)
            travel(node1.right, node2.right)
        }
         
        travel(node1, node2)
        
        return identicalRes;
    }
    
    let subtreeRes: boolean = false;
    
    const travelMain = (node1) => {
        if(subtreeRes === true) return;
        if(node1 === null) return;
        
        if( node1.val === subRoot.val && isIdentical(node1, subRoot)){
            subtreeRes = true
            return
        }
        
        travelMain(node1.left)
        travelMain(node1.right)
    }
   
    travelMain(root)
    
    return subtreeRes;
};
```

## Reference

- [https://leetcode.com/problems/subtree-of-another-tree/](https://leetcode.com/problems/subtree-of-another-tree/)