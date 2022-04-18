---
title: '[LeetCode 62] Unique Paths'
published: true
tags: DynamicProgramming
---

## Problem

There is a robot on an `m x n` grid. The robot is initially located at the
**top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the
**bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either
down or right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to `2 * 10^9`.

### Example 1:

```
Input: m = 3, n = 7
Output: 28
```

### Example 2:

```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```
 
### Constraints:

```
1 <= m, n <= 100
```

## Thoughts

- Typical dynamic programming problem

## TypeScript

```typescript
function uniquePaths(m: number, n: number): number {
    // entry i, j represents number of ways to move to i, j
    const table: number[][] = Array(m + 1).fill(null).map(x => Array(n + 1).fill(0));
    table[1][1] = 1;
    
    for(let i = 1; i <= m; i++){
        for(let j = 1; j <= n; j++){
            if(i === 1 && j === 1) continue;
            // update i, j from sum of left & top
            table[i][j] = table[i - 1][j] + table[i][j - 1]
        }
    }
    
    return table[m][n];
};
```

## Reference

- [https://leetcode.com/problems/unique-paths/](https://leetcode.com/problems/unique-paths/)