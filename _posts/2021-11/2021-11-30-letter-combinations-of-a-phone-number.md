---
title: "[LeetCode 17] Letter Combination of a Phone Number"
published: true
tags: Graph
---

## Problem

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

### Example 1:

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

### Example 2:

```
Input: digits = ""
Output: []
```

### Example 3:

```
Input: digits = "2"
Output: ["a","b","c"]
```

### Constraints:

```
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].
```

## DFS

```typescript
function letterCombinations(digits: string): string[] {
    if(!digits) return []

    const res = []
    const digitToChar = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'qprs',
        8: 'tuv',
        9: 'wxyz'
    }

    const dfs = (i, curStr) => {
        // if we have the string we want, push & return
        if(curStr.length === digits.length) {
            res.push(curStr)
            return
        }

        // for current digit, explore its neighbor
        for(let char of digitToChar[digits[i]]) {
            dfs(i + 1, curStr + char)
        }
    }

    // starts with 0 & empty
    dfs(0, '')

    return res;
};
```

## Reference

- [https://leetcode.com/problems/letter-combinations-of-a-phone-number/](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)