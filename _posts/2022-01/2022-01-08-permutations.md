---
title: '[LeetCode 46] Permutations'
published: true
tags: Backtracking
---

## Problem

Given an array `nums` of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.

### Example 1:

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### Example 2:

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

### Example 3:

```
Input: nums = [1]
Output: [[1]]
```

### Constraints:

- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.

## Thoughts

- We can use backtracking for this
- We can do it recursively

## TypeScript

```typescript
function permute(nums: number[]): number[][] {
    let res: number[][] = [];

    if(nums.length === 1) {
        return [[...nums]]
    }

    // for an array of lenght n, loop n times.
    for(let i of nums){
        // remove the first value
        const first: number = nums.shift()
        // get permutation of remaining array
        const perms: number[][] = permute(nums)
        // add first value back
        for(let perm of perms){
            perm.push(first)
        }
        // update result
        res.push(...perms)
        // move first value to the back
        nums.push(first)
    }
    return res;
};

```

## Reference

- [https://leetcode.com/problems/permutations/](https://leetcode.com/problems/permutations/)