---
title: '[LeetCode 75] Search a 2D Matrix'
published: true
tags: BinarySearch
---

## Problem

Write an efficient algorithm that searches for a value `target` in an `m x n`
integer matrix `matrix`. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.
 
### Example 1:

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

### Example 2:

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```
 
#### Constraints:

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`

## Thoughts

- Binary search in correct row

## TypeScript

```typescript
function searchMatrix(matrix: number[][], target: number): boolean {
    const ROWS: number = matrix.length;
    const COLS: number = matrix[0].length;
    
    for(let i = 0; i < ROWS; i++){
        let l: number = 0, r = COLS - 1;
        // in current row
        if(matrix[i][l] <= target && target <= matrix[i][r]){
            while(l <= r){
                const mid: number = Math.floor((l + r)/2);
                if(matrix[i][mid] === target){
                    return true
                }
                if(matrix[i][mid] < target){
                    l = mid + 1
                } else {
                    r = mid - 1
                }
            }
        } else {
            continue;
        }
    }
    
    return false;
};
```

## Reference

- [https://leetcode.com/problems/search-a-2d-matrix/](https://leetcode.com/problems/search-a-2d-matrix/)