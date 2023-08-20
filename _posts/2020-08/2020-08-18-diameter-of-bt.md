---
title: "Diameter of a Binary Tree"
published: true
tags: Tree
---

## Problem

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
The length of path between two nodes is represented by the number of edges between them.

## Example

	  1
	 / \
	2   3
   / \
  4   5

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

## Thoughts

There are some related things: the height of a node. The height of a node is the number of edges 
on the longest path from the node to a leaf.

So we can find the left child height and right child height, and use them to
find the diameter.

## Code

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {

public:
	int diameter = 0;

public:
	int diameterOfBinaryTree(TreeNode* root) {
		height(root);
		return diameter;
	}

private:
	int height(TreeNode* node) {
		if (node == nullptr) {
			return 0;
		}
		auto leftHeight = height(node->left);
		auto rightHeight = height(node->right);
		diameter = max(diameter, leftHeight + rightHeight);
		return max(leftHeight, rightHeight) + 1;
	}
};
```

## Reference

- [https://leetcode.com/problems/diameter-of-binary-tree/](https://leetcode.com/problems/diameter-of-binary-tree/)