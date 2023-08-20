---
title:  "Maximum Depth of Binary Tree"
published: true
tags: Tree
---

The maximum depth is the number of nodes along the longest path from the root node down to
the farthest leaf node.

## Example

```bash
    3
   / \
  9  20
    /  \
   15   7
```

return its depth = 3

## Thoughts

1. The depth of a node is the maximum depth of its left depth and right depth plus one.
2. Empty node has zero depth.

## Code

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        return depth(root);
    }
    int depth(TreeNode* node){
        if(node == nullptr) {
            return 0;
        }
        auto leftDepth = depth(node->left);
        auto rightDepth = depth(node->right);
        return max(leftDepth, rightDepth) + 1;
    }
};
```

References: [https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
