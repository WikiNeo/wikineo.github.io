---
title: '[LeetCode 217] Contains Duplicate'
published: true
tags: Set
---

## Problem

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

### Example 1:

```
Input: nums = [1,2,3,1]
Output: true
```

### Example 2:

```
Input: nums = [1,2,3,4]
Output: false
```

### Example 3:

```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

### Constraints:

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Thoughts

- We can use `Set` to check for existence

## TypeScript

```typescript
function containsDuplicate(nums: number[]): boolean {
    const s: Set<number> = new Set<number>();
    
    for(let num of nums){
        if(s.has(num)) return true
        else s.add(num)
    }
    
    return false;
};
```

## Reference

- [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/)