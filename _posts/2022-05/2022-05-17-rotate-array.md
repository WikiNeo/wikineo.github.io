---
title: '[LeetCode 189] Rotate Array'
published: true
tags: Others
---

## Problem

Given an array, rotate the array to the right by `k` steps, where `k` is non-negative.

### Example 1:

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

### Example 2:

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```
 
#### Constraints:

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

## Thoughts

- We need move numbers at back to the front
- There should be some nice methods we can use in JavaScript

## TypeScript

```typescript
/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
    nums.unshift(...nums.splice(-(k % nums.length)));
};
```

## Reference

- [https://leetcode.com/problems/rotate-array/](https://leetcode.com/problems/rotate-array/)