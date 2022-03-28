---
title: '[LeetCode 130] Surrounded Regions'
published: true
tags: Graph
---

## Problem

Given an `m x n` matrix `board` containing `'X'` and `'O'`, capture all regions that are 4-directionally surrounded by 'X'.

A region is **captured** by flipping all 'O's into 'X's in that surrounded region.

### Example 1:

```
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
```

### Example 2:

```
Input: board = [["X"]]
Output: [["X"]]
```
 
#### Constraints:

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j] is 'X' or 'O'`.

## TypeScript

```TypeScript
/**
 Do not return anything, modify board in-place instead.
 */
function solve(board: string[][]): void {
    const ROWS: number = board.length;
    const COLS: number = board[0].length;

    // DFS to mark O to T
    const capture = (row: number, col: number): void => {
        if(row < 0 || col < 0 || row >= ROWS || col >= COLS || board[row][col] !== 'O'){
            return;
        }
        board[row][col] = 'T'
        capture(row, col - 1)
        capture(row - 1, col)
        capture(row, col + 1)
        capture(row + 1, col)
    }

    // run capture for all boarder Os
    for(let row = 0; row < ROWS; row++){
        for(let col = 0; col < COLS; col++){
            if((row === 0 || col === 0 || row === ROWS - 1 || col === COLS - 1) && (board[row][col] === 'O')){
                capture(row, col)
            }
        }
    }

    // convert all remaining Os to Xs
    for(let row = 0; row < ROWS; row++){
        for(let col = 0; col < COLS; col++){
            if(board[row][col] === 'O'){
                board[row][col] = 'X'
            }
        }
    }

    // convert all Ts to Os
    for(let row = 0; row < ROWS; row++){
        for(let col = 0; col < COLS; col++){
            if(board[row][col] === 'T'){
                board[row][col] = 'O'
            }
        }
    }
};
```

## Reference

- [https://leetcode.com/problems/surrounded-regions/](https://leetcode.com/problems/surrounded-regions/)