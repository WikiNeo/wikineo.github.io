---
title: '[LeetCode 202] Happy Number'
published: true
tags: Others
---

## Problem

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
- Those numbers for which this process **ends in 1** are happy.

Return `true` if `n` is a happy number, and `false` if not.

### Example 1:

```
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

### Example 2:

```
Input: n = 2
Output: false

```
 
#### Constraints:

- `1 <= n <= 2^31 - 1`

## Thoughts

- Convert the number into string & get sum
- Check sum for result

## TypeScript

```typescript
function isHappy(n: number): boolean { 
    
    while(1){
        let sum: number = n.toString().split('').reduce((acc, value) => {
            const temp: number = parseInt(value)
            return acc + temp*temp
        }, 0)
        if(sum === 1) return true;
        if(sum === 9 || sum === 4) return false;
        n = sum;
    }
};
```

## Reference

- [https://leetcode.com/problems/happy-number/](https://leetcode.com/problems/happy-number/)