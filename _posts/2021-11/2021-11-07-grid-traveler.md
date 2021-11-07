---
title: "[Dynamic Programming] Grid Traveler"
published: true
tags: Algorithm
---

## Problem

You are a traveler on a 2D gird. You begin in the top-left corner and your goal
is to travel to the bottom-right corner. You may only move down or right.

In how many ways can you travel to the gold on a grid with dimensions m*n?

## Brute Force

```javascript
/**
 * @param m rows
 * @param n columns
 * @returns {number|*}  number of ways to travel in grid by moving either downward, or rightward.
 */
const gridTraveler = (m, n) => {
    // base case one: either is 0, means no dimension, then 0 way
    if(m === 0 || n === 0) return 0;
    // base case two: either is 1, means 1 row/column, then 1 way
    if(m === 1 || n === 1) return 1;

    // the ways to move from current node is either
    //  move down m - 1
    //  move right n - 1
    return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)
}
```

### Brute Force Complexity

![Grid Traveler](/../../assets/dynamic-programming/grid-traveler-raw.PNG)

## Memoization

```javascript
const gridTravelerMemo = (m, n, memo = {}) => {
    const key = m + ',' + n;
    if(key in memo) return memo[key]

    if(m === 0 || n === 0) return 0;
    if(m === 1 || n === 1) return 1;

    memo[key] = gridTravelerMemo(m - 1, n, memo) + gridTravelerMemo(m, n - 1, memo)
    return memo[key]
}
```

### Memoization Complexity

![Grid Traveler](/../../assets/dynamic-programming/grid-traveler-memo.PNG)

## Tabulation

```javascript
const gridTravelerTab = (m, n) => {
    const table = Array(m + 1)
        .fill()
        .map(() => Array(n + 1).fill(0))
    table[1][1] = 1;

    for(let i = 0; i <= m; i++){
        for(let j = 0; j <= n; j++) {
            const current = table[i][j];

            // the ways to travel at i, j contributes to
            //  i + 1, j
            //  i, j + 1
            if(i + 1 <= m) table[i + 1][j] += current
            if(j + 1 <= n) table[i][j + 1] += current
        }
    }

    return table[m][n]
}
```

## Reference

- [https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11656s](https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11656s)