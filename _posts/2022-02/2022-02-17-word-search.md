---
title: '[LeetCode 79] Word Search'
published: true
tags: Graph
---

## Problem

Given an `m x n` grid of characters `board` and a string `word`, return `true` if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Example 1:

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

### Example 2:

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

### Example 3:

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```
 
### Constraints:

```
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.
```

## TypeScript

```typescript
function exist(board: string[][], word: string): boolean {
    // it is always good to know the dimension of the 2D board
    const ROW: number = board.length;
    const COL: number = board[0].length;
    
    // we always need a set for dfs
    const visited: Set<string> = new Set<string>();
    
    const dfs = (row: number, col: number, index: number): boolean => {
        // recursive call always has base case
        // good one
        if(index === word.length) return true
        // bad one
        const key: string = `${row},${col}`;
        if(row < 0 || row >= ROW || col < 0 || col >= COL || visited.has(key) || board[row][col] !== word[index]) return false;
        
        // recursive call here
        visited.add(key)
        let res: boolean = ( dfs(row, col - 1, index + 1) ||
                dfs(row - 1, col, index + 1) ||
                dfs(row, col + 1, index + 1) ||
                dfs(row + 1, col, index + 1))
        visited.delete(key)
        return res;
    }
    
    // driver logic
    for(let i = 0; i < ROW; i++){
        for(let j = 0; j < COL; j++){
            if(dfs(i, j, 0) === true) {
                return true
            }
        }
    }
    
    return false;
};
```

## Reference

- [https://leetcode.com/problems/word-search/](https://leetcode.com/problems/word-search/)