---
title: '[LeetCode 36] Valid Sudoku'
published: true
tags: Set
---

## Problem

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

### Note:

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
 
### Example 1:

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

### Example 2:

```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

### Constraints:

```
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'.
```

## Thoughts

- We have row, col, and square to check uniqueness
- Use set for each

## Typescript

```typescript
function isValidSudoku(board: string[][]): boolean {
    let set = new Set()
    
    for(let r = 0; r < board.length; r++) {
        for(let c = 0; c < board[r].length; c++){
            let val = board[r][c]
            
            if(val === '.') continue;
            
            let rowKey = `r: ${r}, val: ${val}`
            let colKey = `c: ${c}, val: ${val}`
            // 3*Math.floor(r/3) + Math.floor(c/3) to get values from 0 to 8, identifying 
            // the 9 large squares, the value in each square must be unique
            let sqrKey = `sqr: ${3*Math.floor(r/3) + Math.floor(c/3)}, val: ${val}`
            
            if(set.has(rowKey) || set.has(colKey) || set.has(sqrKey)) return false;
            
            set.add(rowKey)
            set.add(colKey)
            set.add(sqrKey)
        }
    }
    
    return true;
};
```

## Reference

- [https://leetcode.com/problems/valid-sudoku/](https://leetcode.com/problems/valid-sudoku/)