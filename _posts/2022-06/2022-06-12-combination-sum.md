---
title: '[LeetCode 39] Combination Sum'
published: true
tags: Backtracking
---

## Problem

Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target`. You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is **guaranteed** that the number of unique combinations that sum up to `target` is less than 150 combinations for the given input.

### Example 1:

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

### Example 2:

```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

### Example 3:

```
Input: candidates = [2], target = 1
Output: []
```

#### Constraints:

- `1 <= candidates.length <= 30`
- `1 <= candidates[i] <= 200`
- All elements of `candidates` are **distinct**.
- `1 <= target <= 500`

## Thoughts

- For each number in `candidates`, we can either include it or not include it,
  this affects the total sum & how we move the pointer
- Total sum/remain is the success condition, and pointer location at the end
  or invalid sum/remain value is the fail condition

## TypeScript

```typescript
function combinationSum(candidates: number[], target: number): number[][] {
    const LEN: number = candidates.length;
    const res: number[][] = []
    
    const candidate: number[] = []
    const dfs = (i: number, remain: number) => {
       
        if(remain === 0) {
            res.push([...candidate])
            return
        }
         if(i === LEN || remain < 0) return;
        
        // using current number
        candidate.push(candidates[i])
        // duplicate
        dfs(i, remain - candidates[i])
        
        // not using current number, move to next
        candidate.pop()
        dfs(i + 1, remain)
    }
    
    dfs(0, target)
    
    return res;
};
```

## Reference

- [https://leetcode.com/problems/combination-sum/](https://leetcode.com/problems/combination-sum/)