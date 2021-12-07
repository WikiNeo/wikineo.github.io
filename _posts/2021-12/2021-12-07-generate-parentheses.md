---
title: '[LeetCode 22] Generate Parentheses'
published: true
tags: Array
---

## Problem

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### Example 1:

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

### Example 2:

```
Input: n = 1
Output: ["()"]
```

### Constraints:

```
1 <= n <= 8
```

## Thoughts

- In a valid result, the number of left bracket should be less than n
- The number of right bracket should be less than left

## Typescript

```typescript
function generateParenthesis(n: number): string[] {
    const res = []

    const generate = (str = '', left = 0, right = 0) => {
        if(left === n && right === n) {
            res.push(str)
            return
        }
        if(left < n) {
            generate(str + '(', left + 1, right)
        }
        if(right < left) {
            generate(str + ')', left, right + 1)
        }
    }

    generate()
    return res;
}
```

## Reference

- [https://leetcode.com/problems/generate-parentheses/](https://leetcode.com/problems/generate-parentheses/)