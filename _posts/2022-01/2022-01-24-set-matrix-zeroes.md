---
title: '[LeetCode 73] Set Matrix Zeroes'
published: true
tags: Others
---

## Problem

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s, and return the matrix.

You must do it in place.

### Example 1:

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

### Example 2:

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```
 
### Constraints:

```
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -231 <= matrix[i][j] <= 231 - 1
```

## TypeScript

```typescript
/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
    const rowLen: number = matrix.length;
    const colLen: number = matrix[0].length;
    let rowZero: boolean = false; // flag indicates if we will set row 0 to 0s

    for(let i = 0; i < rowLen; i++){
        for(let j = 0; j < colLen; j++){
            if(matrix[i][j] === 0) {
                // use first row to determine which columns to set to 0s
                matrix[0][j] = 0;
                
                if(i === 0){
                    rowZero = true;
                } else {    
                    // use first column to determine which rows except row 0 to set to 0s;
                    matrix[i][0] = 0;
                }
            }
        }
    }

    // set everything except the first row & column
    for(let i = 1; i < rowLen; i++){
        for(let j = 1; j < colLen; j++){
            if(matrix[0][j] === 0 || matrix[i][0] === 0){
                matrix[i][j] = 0;
            }
        }
    }

    // set first column
    if(matrix[0][0] === 0){
        for(let i = 0; i < rowLen; i++){
            matrix[i][0] = 0;
        }
    }

    // set first row
    if(rowZero){
        for(let j = 0; j < colLen; j++){
            matrix[0][j] = 0;
        }
    }
};
```

## Reference

- [https://leetcode.com/problems/set-matrix-zeroes/](https://leetcode.com/problems/set-matrix-zeroes/)