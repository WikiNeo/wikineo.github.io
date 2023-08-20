---
title: '[LeetCode 102] Binary Tree Level Order Traversal'
published: true
tags: Tree
---

## Problem

Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

### Example 1:

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

### Example 2:

```
Input: root = [1]
Output: [[1]]
```

### Example 3:

```
Input: root = []
Output: []
```
 
### Constraints:

```
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000
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

function levelOrder(root: TreeNode | null): number[][] {
    let res: number[][] = [];
    let queue: TreeNode[] = [];
    let count: number = 1;
    queue.push(root);
    
    while(queue.length !== 0){
        let temp: number[] = [];
        const SIZE: number = queue.length
        
        for(let i = 0; i < SIZE; i++){
            let front: TreeNode = queue.shift();
            if(front !== null){
                temp.push(front.val)
                queue.push(front.left);
                queue.push(front.right);
            }
        }
        
        count *= 2;
        
        if(temp.length !== 0) res.push(temp);
    }
    
    return res;
};
```

## Reference

- [https://leetcode.com/problems/binary-tree-level-order-traversal/](https://leetcode.com/problems/binary-tree-level-order-traversal/)