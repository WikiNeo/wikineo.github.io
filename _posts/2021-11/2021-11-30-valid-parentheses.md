---
title: "[LeetCode 20] Valid Parentheses"
published: true
tags: Stack
---

## Problem

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
### Example 1:

```
Input: s = "()"
Output: true
```

### Example 2:

```
Input: s = "()[]{}"
Output: true
```

### Example 3:

```
Input: s = "(]"
Output: false
```

### Example 4:

```
Input: s = "([)]"
Output: false
```

### Example 5:

```
Input: s = "{[]}"
Output: true
```
 
### Constraints:

```
- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.
```

## Typescript

```typescript
function isValid(s: string): boolean {
    if(s.length % 2 === 1) return false;

    const stack = []
    const leftBrackets = ['(', '[', '{']

    for(let p of s) {
        // push to stack if it is left brackets
        if(leftBrackets.includes(p)) {
            stack.push(p)
        } else {
            // pop if it is right brackets and do order check
            const current = stack.pop()
            if(!(
                (p === ')' && current === '(') ||
                (p === ']' && current === '[' ) ||
                (p === '}' && current === '{')
            )
            ){
                return false;
            }
        }
    }

    // there maybe only left brackets
    return stack.length === 0;
};
```

## Reference

- [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)