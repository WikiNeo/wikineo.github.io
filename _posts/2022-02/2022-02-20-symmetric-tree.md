---
title: '[LeetCode 101] Symmetric Tree'
published: true
tags: BinaryTree
---

## Problem

Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

### Example 1:

```
Input: root = [1,2,2,3,4,4,3]
Output: true
```

### Example 2:

```
Input: root = [1,2,2,null,3,null,3]
Output: false
```
 
### Constraints:

```
- The number of nodes in the tree is in the range [1, 1000].
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

function isSymmetric(root: TreeNode | null): boolean {
    let queue: TreeNode[] = [];
    queue.push(root.left);
    queue.push(root.right);
    
    while(queue.length !== 0) {
        const LEN: number = queue.length;
        
        for(let i = 0; i < LEN/2; i++){
            let front: TreeNode = queue.shift();
            let end: TreeNode = queue.pop();
            
            if(front === null && end === null) continue;
            if((front === null && end !== null) || (front !== null && end === null) || (front.val !== end.val)) return false;
            
            queue.unshift(front.left);
            queue.unshift(front.right);
            queue.push(end.right)
            queue.push(end.left);
        }
    }
    
    return true;
};
```

## Reference

- [https://leetcode.com/problems/symmetric-tree/](https://leetcode.com/problems/symmetric-tree/)