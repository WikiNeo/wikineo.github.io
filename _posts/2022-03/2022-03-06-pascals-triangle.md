---
title: '[LeetCode 118] Pascals Triangle'
published: true
tags: Recursion
---

## Problem

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

### Example 1:

```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

### Example 2:

```
Input: numRows = 1
Output: [[1]]
```
 
#### Constraints:

```
- 1 <= numRows <= 30
```

## TypeScript

```TypeScript
function generate(numRows: number): number[][] {
    let res: number[][] = [];
    
    const build = (num: number, parent: number[]): void => {
        if(num === numRows + 1) {
            return;
        }
        
        let temp: number[] = []
        
        for(let i = 0; i < num; i++){
            if(i === 0 || i === num - 1){
                temp.push(1)
            } else {
                temp.push(parent[i - 1] + parent[i]);    
            }
        }
        
        res.push(temp)
        build(num + 1, temp)
    }
    
    build(1, [])
    return res;
};
```

## Reference

- [https://leetcode.com/problems/pascals-triangle/](https://leetcode.com/problems/pascals-triangle/)