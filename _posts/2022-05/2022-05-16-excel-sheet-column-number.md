---
title: '[LeetCode 171] Excel Sheet Column Number'
published: true
tags: Others
---

## Problem

Given a string `columnTitle` that represents the column title as appear in an
Excel sheet, return its corresponding column number.

For example:

```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
```

### Example 1:

```
Input: columnTitle = "A"
Output: 1
```

### Example 2:

```
Input: columnTitle = "AB"
Output: 28
```

### Example 3:

```
Input: columnTitle = "ZY"
Output: 701
```
 
#### Constraints:

- `1 <= columnTitle.length <= 7`
- `columnTitle` consists only of uppercase English letters.
- `columnTitle` is in the range `["A", "FXSHRXW"]`.

## Thoughts

- Find char code
- 26 base number

## TypeScript

```typescript
function titleToNumber(columnTitle: string): number {
    let res = 0;
    let power = 0;
    const charCodeA: number = 'A'.charCodeAt(0)
    
    for(let i = columnTitle.length - 1; i >=0; i--){
        res += (26**power * (columnTitle.charCodeAt(i) - charCodeA + 1))
        power++;
    }
    
    return res;
};
```

## Reference

- [https://leetcode.com/problems/excel-sheet-column-number/](https://leetcode.com/problems/excel-sheet-column-number/)