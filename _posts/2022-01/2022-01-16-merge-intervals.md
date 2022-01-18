---
title: '[LeetCode 56] Merge Intervals'
published: true
tags: Sorting
---

## Problem

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Example 1:

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

### Example 2:

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```
 
### Constraints:

```
- 1 <= intervals.length <= 104
- intervals[i].length == 2
- 0 <= starti <= endi <= 104
```

## Thoughts

- We can sort the intervals first
- Then compare start value of current interval with previous one

## TypeScript

```TypeScript
function merge(intervals: number[][]): number[][] {
    // sort intervals by starting index
    intervals.sort((a, b) => a[0] - b[0])
    // initialize result with first interval
    let res: number[][] = [intervals[0]]
    
    for(let interval of intervals){
        const start: number = interval[0]
        const end: number = interval[1]
        const lastEnd: number = res[res.length - 1][1];
        
        if(start <= lastEnd) {  // we have an overlap
            res[res.length - 1][1] = Math.max(lastEnd, end)
        } else {
            res.push([start, end])
        }
    }
    
    return res;
};
```

## Reference

- [https://leetcode.com/problems/merge-intervals/](https://leetcode.com/problems/merge-intervals/)