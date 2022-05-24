---
title: '[LeetCode 128] Longest Consecutive Sequence'
published: true
tags: Set
---

## Problem

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

### Example 1:

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

### Example 2:

```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```
 
### Constraints:

- `0 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`

## Thoughts

- To find the consecutive sequence, we need find the start number
- The start number should be such that startNumber - 1 doesn't exist in array
- For existence check, we can use Set

## TypeScript

```typescript
function longestConsecutive(nums: number[]): number {
    let result: number = 0;
    const sNum: Set<number> = new Set(nums);
    
    for(let num of nums) {
        // find the start
        if(!sNum.has(num - 1)){
            // update the consecutive sequence count
            let temp = 0;
            while(sNum.has(num + temp)){
                temp++;
            }
            result = Math.max(result, temp)
        }
    }
    
    return result;
};
```

## Reference

- [https://leetcode.com/problems/longest-consecutive-sequence/](https://leetcode.com/problems/longest-consecutive-sequence/)