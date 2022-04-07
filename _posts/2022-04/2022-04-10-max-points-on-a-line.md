---
title: '[LeetCode 149] Max Points on a Line'
published: true
tags: Others
---

## Problem

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane, return the maximum number of points that lie on the same straight line.

### Example 1:

```
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
```

### Example 2:

```
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
```
 
### Constraints:

- `1 <= points.length <= 300`
- `points[i].length == 2`
- `-10^4 <= xi, yi <= 10^4`
- All the `points` are **unique**.

## Thoughts

- Same slope means point on the line
- Vertical line is special case

## TypeScript

```TypeScript
function maxPoints(points: number[][]): number {
    if(points.length < 3) {
        return points.length;
    }
    
    let res = 0;
    
    for(let i = 0; i < points.length; i++){
        const slopes: {[index: number]: number} = {Infinity: 0}
        for(let j = i + 1; j < points.length; j++){
            const xDiff = points[i][0] - points[j][0];
            const yDiff = points[i][1] - points[j][1];
            const slope = xDiff === 0 ? Infinity : yDiff/xDiff;
            
            // same slope means more points on a line
            slope in slopes ? slopes[slope]++ : slopes[slope] = 1
            
            res = Math.max(res, slopes[slope])
        }
    }
    
    // we didn't count the first point, so add 1
    return res + 1;
};
```

## Reference

- [https://leetcode.com/problems/max-points-on-a-line/](https://leetcode.com/problems/max-points-on-a-line/)