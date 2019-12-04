---
title: "Construct Binary Tree from Preorder and Inorder Traversal"
published: true
---

Given preorder and inorder traversal of a tree, construct the binary tree.

## Example

Given

```bash
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```

we get

```bash
    3
   / \
  9  20
    /  \
   15   7
```

## Thoughts

1. The first element in preorder array is the root of the tree.
2. each element in preorder array divides the tree into the left part and right part

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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int, int> inorderValueToIndex;
        
        for(auto i = 0; i < inorder.size(); i++){
            inorderValueToIndex[inorder[i]] = i;
        }
        
        auto preorderIndex = 0;
        auto root = build(0, preorder.size() - 1, inorderValueToIndex, preorderIndex, preorder);
        
        return root;
    }
    TreeNode* build(int start, int end, unordered_map<int, int>& inorderValueToIndex, int& preorderIndex, vector<int>& preorder){
        if(start > end) {
            return nullptr;
        }
        
        auto val = preorder[preorderIndex++];
        auto node = new TreeNode(val);
        auto mid = inorderValueToIndex[val];
        
        node->left = build(start, mid - 1, inorderValueToIndex, preorderIndex, preorder);
        node->right = build(mid + 1, end, inorderValueToIndex, preorderIndex, preorder);
        
        return node;
    }
};
```

Reference: [https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
