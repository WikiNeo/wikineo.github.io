---
title: '[LeetCode 200] Number of Islands'
published: true
tags: Graph
---

## Problem

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

### Example 1:

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

### Example 2:

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```
 
#### Constraints:

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

## Thoughts

- 2D Array DFS, returns true when we finished visiting an island and increase count by 1
- Boundary, water & visited for base case return

## TypeScript

```typescript
function numIslands(grid: string[][]): number {
    const ROWS: number = grid.length;
    const COLS: number = grid[0].length;
    let count: number = 0;
    let visited: Set<string> = new Set<string>();
    
    // dfs explore
    // return true if we can use (row, col) as a starting point and find an unvisited island;
    const explore = (row: number, col: number): boolean => {
        // base case;
        // out of bound
        if(!(row >= 0 && row < ROWS)) return false;
        if(!(col >= 0 && col < COLS)) return false;
        // water
        if(grid[row][col] === '0') return false;
        // visited
        const coord: string = `${row},${col}`;
        if(visited.has(coord)){
            return false;
        }
        
        // explore now
        visited.add(coord);
        explore(row, col - 1)
        explore(row - 1, col)
        explore(row, col + 1)
        explore(row + 1, col)
        
        return true;
    }
    
    // driver function
    for(let i = 0; i < ROWS; i++){
        for(let j = 0; j < COLS; j++){
            if(explore(i, j) === true){
                count++;
            }
        }
    }
    
    return count;
};
```

## Reference

- [https://leetcode.com/problems/number-of-islands/](https://leetcode.com/problems/number-of-islands/)