---
title: '[LeetCode 287] Find the Duplicate Number'
published: true
tags: Array
---

## Problem

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return this repeated number.

You must solve the problem **without** modifying the array `nums` and uses only constant extra space.

### Example 1:

```
Input: nums = [1,3,4,2,2]
Output: 2
```

### Example 2:

```
Input: nums = [3,1,3,4,2]
Output: 3
```
 
#### Constraints:

- `1 <= n <= 105`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.
 
#### Follow up:

- How can we prove that at least one duplicate number must exist in `nums`?
- Can you solve the problem in linear runtime complexity?

## Thoughts

- Let's use slow & fast pointer to find the start of cycle

## TypeScript

```typescript
function findDuplicate(nums: number[]): number {
    let slow: number = 0, fast: number = 0;
    
    // find intersection of slow & fast
    while(true){
        slow = nums[slow]
        fast = nums[nums[fast]]
        if (slow === fast){
            break;
        }
    }
    
    // find the start of cycle
    let slow2: number = 0;
    while(true){
        slow = nums[slow]
        slow2 = nums[slow2]
        if(slow === slow2) {
            return slow;
        }
    }
};
```

## Reference

- [https://leetcode.com/problems/find-the-duplicate-number/](https://leetcode.com/problems/find-the-duplicate-number/)