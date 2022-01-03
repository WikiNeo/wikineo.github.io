---
title: '[LeetCode 42] Trapping Rain Water'
published: true
tags: TwoPointers
---

## Problem

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

### Example 1:

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

### Example 2:

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

### Constraints:

```
- n == height.length
- 1 <= n <= 2 * 104
- 0 <= height[i] <= 105
```

## Typescript

```typescript
function trap(height: number[]): number {
    let l = 0, r = height.length - 1
    
    // we store leftMax as first value and rightMax as last value
    let leftMax = height[l], rightMax = height[r]
    let res = 0;
    
    // we have to pointers moving to the mid
    while (l < r) {
        // decide which pointer to move
        if(leftMax < rightMax) {
            l++;
            // update max value
            leftMax = Math.max(leftMax, height[l])
            // update res
            res += leftMax - height[l];
        } else {
            r--;
            rightMax = Math.max(rightMax, height[r])
            res += rightMax - height[r]
        }
    }
    return res;
};
```

## Reference

- [https://leetcode.com/problems/trapping-rain-water/](https://leetcode.com/problems/trapping-rain-water/)