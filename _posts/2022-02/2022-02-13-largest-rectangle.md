---
title: '[LeetCode 84] Largest Rectangle in Histogram'
published: true
tags: Stack
---

## Problem

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

### Example 1:

```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```

### Example 2:

```
Input: heights = [2,4]
Output: 4
```
 
### Constraints:

```
1 <= heights.length <= 105
0 <= heights[i] <= 104
```

## TypeScript

```typescript
function largestRectangleArea(heights: number[]): number {
    let maxArea: number = 0;
    // stores [startIndex, height] of a histogram
    let stack: number[][] = [];
    
    for(let i = 0; i < heights.length; i++){
        const height: number = heights[i];
        // let's assume the startIndex is the same as current index first
        let startIndex: number = i;
        
        // while current height is less than the top height in stack
        while(stack.length !== 0 && stack[stack.length - 1][1] > height){
            const top: number[] = stack.pop()
            const topIndex: number = top[0]
            const topHeight: number = top[1]
            // calculate the furthest left we can get
            maxArea = Math.max(maxArea, (i - topIndex) * topHeight)
            startIndex = topIndex
        }
        stack.push([startIndex, height])
    }
    
    // we still have increasing elements which can extend to the end in stack
    for(let data of stack){
        maxArea = Math.max(maxArea, (heights.length - data[0]) * data[1])
    }
    
    return maxArea
};
```

## Reference

- [https://leetcode.com/problems/largest-rectangle-in-histogram/](https://leetcode.com/problems/largest-rectangle-in-histogram/)