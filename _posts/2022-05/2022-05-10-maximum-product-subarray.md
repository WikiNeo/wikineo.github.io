---
title: '[LeetCode 152] Maximum Product Subarray'
published: true
tags: DynamicProgramming
---

## Problem

Given an integer array `nums`, find a contiguous non-empty subarray within the
array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a **32-bit** integer.

A **subarray** is a contiguous subsequence of the array.

### Example 1:

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

### Example 2:

```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```
 
#### Constraints:

- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any prefix or suffix of nums is **guaranteed** to fit in a **32-bit** integer.

## Thoughts

- We can store current min & max
- Reset current min & max when we have 0

## TypeScript

```typescript
function maxProduct(nums: number[]): number {
    // set default value
    let res: number = Math.max(...nums);
    let curMin: number = 1, curMax: number = 1;
    
    for(let num of nums){
        if(num === 0){
            curMin = 1
            curMax = 1
            continue;
        }
        const temp: number = num*curMax;
        curMax = Math.max(num*curMax, num*curMin, num);
        curMin = Math.min(temp, num*curMin, num)
        res = Math.max(res, curMax)
    }
    
    return res;
};
```

## Reference

- [https://leetcode.com/problems/maximum-product-subarray/](https://leetcode.com/problems/maximum-product-subarray/)
