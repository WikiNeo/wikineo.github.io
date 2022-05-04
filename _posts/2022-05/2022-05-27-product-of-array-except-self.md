---
title: '[LeetCode 238] Product of Array Except Self'
published: true
tags: Array
---

## Problem

Given an integer array `nums`, return an array `answer` such that `answer[i]` is
equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

### Example 1:

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

### Example 2:

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```
 
#### Constraints:

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.
 

#### Follow up

Can you solve the problem in `O(1)` extra space complexity? (The output array
**does not** count as extra space for space complexity analysis.)

## Thoughts

- We store preSum & postSum in result array

## TypeScript

```typescript
function productExceptSelf(nums: number[]): number[] {
    const res: number[] = [];
    
    let prefix: number = 1;
    for(let i = 0; i < nums.length; i++){
        if(i === 0){
            res[i] = 1;
        } else {
            prefix *= nums[i - 1]
            res[i] = prefix;
        }
    }
    
    let postfix: number = 1;
    for(let i = nums.length - 2; i >= 0; i--){
        postfix *= nums[i + 1]
        res[i] *= postfix;
    }
    
    return res;
};
```

## Reference

- [https://leetcode.com/problems/product-of-array-except-self/](https://leetcode.com/problems/product-of-array-except-self/)