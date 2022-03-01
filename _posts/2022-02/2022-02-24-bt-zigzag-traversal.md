---
title: '[LeetCode 103] Binary Tree Zigzag Level Order Traversal'
published: true
tags: BinaryTree
---

## Problem

Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

### Example 1:

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
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

function zigzagLevelOrder(root: TreeNode | null): number[][] {
    let res: number[][] = [];
    let isReverse: boolean = false;
    let queue: TreeNode[] = [];
    
    queue.push(root);
    while(queue.length !== 0) {
        let temp: number[] = [];
        const LEN: number = queue.length;
        
        for(let i = 0; i < LEN; i++){
            const front: TreeNode = queue.shift();
            if(front !== null){
                temp.push(front.val);
                queue.push(front.left);
                queue.push(front.right);
            }
        }
        
        if(temp.length !== 0) {
            if(isReverse){
                temp.reverse()
            }
            isReverse = !isReverse;
            res.push(temp)
        }
    }
    
    return res;
};
```

## Reference

- [https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)