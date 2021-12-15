---
title: '[LeetCode 34] Find First and Last Position of Element in Sorted Array'
published: true
tags: BinarySearch
---

## Problem

Given an array of integers `nums` sorted in non-decreasing order, find the
starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1:

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

### Example 2:

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

### Example 3:

```
Input: nums = [], target = 0
Output: [-1,-1]
```
 
### Constraints:

```
- 0 <= nums.length <= 105
- -109 <= nums[i] <= 109
- nums is a non-decreasing array.
- -109 <= target <= 109
```

## Thoughts

- Modified binary search

## Typescript

```typescript
function searchRange(nums: number[], target: number): number[] {
    const binSearch = (nums, target, leftBias) => {
        let l = 0, r = nums.length - 1;

        let res = -1;
        while(l <= r) {
            let m = Math.floor((l + r)/2)

            
            if(target < nums[m]){
                r = m - 1
            } else if(target > nums[m]){
                l = m + 1
            } else {
                res = m
                // trying to find left most index
                if(leftBias) {
                    r = m - 1
                } else {
                    l = m + 1
                }
            }
        }
        
        return res;
    }
    
    return [binSearch(nums, target, true), binSearch(nums, target, false)]
};
```

## Reference

- [https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)