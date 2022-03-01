---
title: '[LeetCode 75] Sort Colors'
published: true
tags: TwoPointers
---

## Problem

Given an array `nums` with `n` objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in the
order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

### Example 1:

```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

### Example 2:

```
Input: nums = [2,0,1]
Output: [0,1,2]
```
 
### Constraints:

```
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2.
```

- Follow up: Could you come up with a one-pass algorithm using only constant extra space?

## TypeScript

```TypeScript
/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
    const swap = (i: number, j: number): void => {
        let temp: number = nums[i];
        nums[i] = nums[j]
        nums[j] = temp;
    }
    let l: number = 0;
    let r: number = nums.length - 1;
    let i: number = 0;

    while(i <= r){
        if(nums[i] === 0) {
            swap(l, i);
            l++;
        }else if(nums[i] === 2){
            swap(r, i);
            r--;
            i--;
        }
        i++;
    }
};
```

## Reference

- [https://leetcode.com/problems/sort-colors/](https://leetcode.com/problems/sort-colors/)