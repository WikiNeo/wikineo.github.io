---
title: '[LeetCode 54] Spiral Matrix'
published: true
tags: TwoPointers
---

## Problem

Given an `m x n` matrix, return all elements of the `matrix` in spiral order.

### Example 1:

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

### Example 2:

```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```
 
### Constraints:

```
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100
```

## Thoughts

- Try to use double pointers for matrix problem
- We can process each row/column in a loop

## TypeScript

```TypeScript
function spiralOrder(matrix: number[][]): number[] {
    let left: number = 0, right: number = matrix[0].length;
    let top: number = 0, bottom: number = matrix.length;
    let res: number[] = [];
    
    while (left < right && top < bottom){
        // top row
        for(let j = left; j < right; j++){
            res.push(matrix[top][j])
        }
        top++;
        
        // right column
        for(let i = top; i < bottom; i++){
            res.push(matrix[i][right - 1])
        }
        right--;
        
        // check break condition
        if(!(left < right && top < bottom)){
            break;    
        }
        
        // bottom row
        for(let j = right - 1; j >= left; j--){
            res.push(matrix[bottom - 1][j])
        }
        bottom--;
        
        // left column
        for(let i = bottom - 1; i >= top; i--){
            res.push(matrix[i][left])
        }
        left++;
    }
    // return result
    return res;
};
```

## Reference

- [https://leetcode.com/problems/spiral-matrix/](https://leetcode.com/problems/spiral-matrix/)