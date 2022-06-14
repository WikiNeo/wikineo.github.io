---
title: '[LeetCode 40] Combination Sum'
published: true
tags: Backtracking
---

## Problem

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

Note: The solution set must not contain duplicate combinations.

### Example 1:

```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

### Example 2:

```
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```
 
#### Constraints:

- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Thoughts

- Sum equaling `target` is the success condition, pointer out of bound or sum
  being larger than `target` is the fail condition.
- We can either include one value, or skip all its duplicates

## TypeScript

```typescript
function combinationSum2(candidates: number[], target: number): number[][] {
    const res: number[][] = []
    const LEN: number = candidates.length;
    
    candidates.sort((a, b) => a - b)
    const combination: number[] = []
    const exec = (i: number, sum: number) => {
        
        if(sum === target) {
            res.push([...combination])
            return;
        }
        if(i === LEN || sum > target) return;
        
        combination.push(candidates[i])
        exec(i + 1, sum + candidates[i])
        combination.pop()
        
        while(i + 1 < LEN && candidates[i] === candidates[i + 1]) i++
        exec(i + 1, sum)
    }
    
    exec(0, 0)
    
    return res;
};
```

## Reference

- [https://leetcode.com/problems/combination-sum-ii/](https://leetcode.com/problems/combination-sum-ii/)