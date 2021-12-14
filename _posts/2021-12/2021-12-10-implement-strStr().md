---
title: '[LeetCode 28] Implement strStr()'
published: true
tags: TwoPointers
---

## Problem

Implement `strStr()`.

Return the index of the first occurrence of needle in haystack, or `-1` if `needle` is not part of `haystack`.

### Clarification:

What should we return when `needle` is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty
string. This is consistent to C's `strstr()` and Java's `indexOf()`.
 
### Example 1:

```
Input: haystack = "hello", needle = "ll"
Output: 2
```

### Example 2:

```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

### Example 3:

```
Input: haystack = "", needle = ""
Output: 0
```

### Constraints:

```
- 0 <= haystack.length, needle.length <= 5 * 104
- haystack and needle consist of only lower-case English characters.
```

## Thoughts

- We can find the first character in haystack that is the same as the first one
  in needle, then checking if the following characters are the same

## Typescript

```typescript
function strStr(haystack: string, needle: string): number {
    if(needle.length === 0) return 0;
    
    let res = -1;
    
    for(let i = 0; i < haystack.length; i++){
        if(res !== -1) break;
        // we can check needle here
        if(haystack[i] === needle[0]) {
            let temp = true
            // check next few characters in haystack with needle
            for(let j = i + 1; j < needle.length + i; j++) {
                if(haystack[j] !== needle[j - i]) {
                    temp = false;
                }
            }
            if(temp) {
                res = i;
                return res;
            }
        }
    }
    
    return res;
};
```

## Reference

- [https://leetcode.com/problems/implement-strstr/](https://leetcode.com/problems/implement-strstr/)