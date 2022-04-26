---
title: '[LeetCode 162] Find Peak Element'
published: true
tags: BinarySearch
---

## Problem

A peak element is an element that is strictly greater than its neighbors.

Given an integer array `nums`, find a peak element, and return its index. If
the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`.

You must write an algorithm that runs in `O(log n)` time.

### Example 1:

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

### Example 2:

```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```
 
### Constraints:

- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`.

## Thoughts

- Try binary search?
- Draw a graph for the array?

## TypeScript

```typescript
function findPeakElement(nums: number[]): number {
    let l: number = 0, r = nums.length - 1;
    
    while(l < r){
        let mid: number = Math.floor((l + r)/2);
    
        // we are in decreasing line
        if(nums[mid] > nums[mid + 1]){
            r = mid
        } else {
            l = mid + 1
        }
    }
    return l
};
```

## Reference

- [https://leetcode.com/problems/find-peak-element/](https://leetcode.com/problems/find-peak-element/)