---
title: '[LeetCode 289] '
published: true
tags: Array
---

## Problem

According to Wikipedia's article: "The Game of Life, also known simply as
Life, is a cellular automaton devised by the British mathematician John Horton
Conway in 1970."

The board is made up of an `m x n` grid of cells, where each cell has an initial
state: **live** (represented by a `1`) or **dead** (represented by a `0`). Each cell
interacts with its eight neighbors (horizontal, vertical, diagonal) using the
following four rules (taken from the above Wikipedia article):

- Any live cell with fewer than two live neighbors dies as if caused by under-population.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by over-population.
- Any dead cell with exactly three live neighbors becomes a live cell, as if
  by reproduction.

The next state is created by applying the above rules simultaneously to every
cell in the current state, where births and deaths occur simultaneously. Given
the current state of the `m x n` grid `board`, return the next state.

### Example 1:

```
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
```

### Example 2:

```
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
```
 
#### Constraints:

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 25`
- `board[i][j]` is `0` or `1`.
 

#### Follow up:

- Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
- In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

## Thoughts

- Let's do some mapping
  - 0->0 2
  - 0->1 3
  - 1->0 4
  - 1->1 5

## TypeScript

```typescript
/**
 Do not return anything, modify board in-place instead.
 */
function gameOfLife(board: number[][]): void {
    const ROWS: number = board.length;
    const COLS: number = board[0].length;

    const countLives = (row: number, col: number): number => {
        let res: number = 0;
        for(let i = -1; i <= 1; i++){
            for(let j = -1; j <= 1; j++){
                if(!(i === 0 && j=== 0)){
                    const tempR: number = row + i
                    const tempC: number = col + j;
                    if(tempR < 0 || tempR >= ROWS || tempC < 0 || tempC >= COLS){
                        continue;
                    }
                    if(board[tempR][tempC] === 1 || board[tempR][tempC] === 4 || board[tempR][tempC] === 5) {
                        res++;
                    }
                }
            }
        }
        
        return res;
    }
    
    const setTempValues = (row: number, col: number, cur: number, liveCount: number): void => {
        if(cur === 0 || cur === 2 || cur === 3){
            if(liveCount === 3){
                board[row][col] = 3
            } else {
                board[row][col] = 2
            }
        } else {
            if(liveCount === 2 || liveCount === 3){
                board[row][col] = 5
            } else {
                board[row][col] = 4;
            }
        }
    }
    /*
    0->0 2
    0->1 3
    1->0 4
    1->1 5
    */
    for(let i = 0; i < ROWS; i++){
        for(let j = 0; j < COLS; j++){
            setTempValues(i, j, board[i][j], countLives(i, j))
        }
    }

    for(let i = 0; i < ROWS; i++){
        for(let j = 0; j < COLS; j++){
            const value: number = board[i][j]
            if(value === 2 || value === 4){
                board[i][j] = 0
            } else {
                board[i][j] = 1;
            }
        }
    }
};
```

## Reference

- [https://leetcode.com/problems/game-of-life/](https://leetcode.com/problems/game-of-life/)