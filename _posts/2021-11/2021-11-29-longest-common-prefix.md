---
title: "[LeetCode 14] Longest Common Prefix"
published: true
tags: TwoPointers
---

## Problem

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

### Example 1:

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

### Example 2:

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```
 
### Constraints:

```
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lower-case English letters.
```

## Typescript

```typescript
function longestCommonPrefix(strs: string[]): string {
    // if the strs is less than 1, return the first
    if(strs.length <= 1) return strs[0];

    // let's assume the first as the prefix, and start from the beginning
    for(let i = 0; i < strs[0].length; i++) {
        // we compare each character in first str to the rest
        for(let j = 1; j < strs.length; j++) {
            // return if we are at the end of the string or they don't match
            if(i === strs[j].length || strs[0][i] !== strs[j][i]) {
                return strs[0].substring(0, i)
            }
        }
    }

    // if all are the same
    return strs[0];
};
```

## Reference

- [https://leetcode.com/problems/longest-common-prefix/](https://leetcode.com/problems/longest-common-prefix/)