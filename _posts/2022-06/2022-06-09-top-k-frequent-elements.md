---
title: '[LeetCode 347] Top K Freuquent Elements'
published: true
tags: Hash
---

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

### Example 1:

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

### Example 2:

```
Input: nums = [1], k = 1
Output: [1]
```

#### Constraints:

- `1 <= nums.length <= 105`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is **unique**.
 
#### Follow up:

Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## Thoughts

- O(N) value to count
- O(UlogU) sort where U is number of unique elements

## TypeScript

```typescript
function topKFrequent(nums: number[], k: number): number[] {
    const valueToCount: Map<number, number> = new Map<number, number>();
    
    for(const num of nums){
        const count: number = valueToCount.get(num) || 0
        valueToCount.set(num, count + 1)
    }
    
    return [...valueToCount.entries()].sort((a, b) => b[1] - a[1]).slice(0, k).map(entry => entry[0])
};
```

## Reference

- [https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/)