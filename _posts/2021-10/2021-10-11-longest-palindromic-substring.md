---
title: "[LeetCode 5] Longest Palindromic Substring"
published: true
tags: TwoPointers
---

## Problem

Given a string s, return the longest palindromic substring in s.

### Example 1:

```
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

### Example 2:

```
Input: s = "cbbd"
Output: "bb"
```

### Example 3:

```
Input: s = "a"
Output: "a"
```

### Example 4:

```
Input: s = "ac"
Output: "a"
```

### Constraints:

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

## Thoughts

- We can check for palindromic substring from center, and move to left & right
- We need handle even and odd case

## Code

```typescript
function longestPalindrome(s: string): string {
    let res = ""
    let resLen = 0
    
    for(let i = 0; i < s.length; i++) {
        
        // odd palindrome case
        let l = i, r = i
        while (l >= 0 && r < s.length && s[l] === s[r]) {
            if(r - l + 1 > resLen) {
                res = s.substring(l, r + 1)
                resLen = r - l + 1
            }
            l -= 1
            r += 1
        }
        
        // even case
        l = i, r = i + 1
        while (l >= 0 && r < s.length && s[l] === s[r]) {
            if(r - l + 1 > resLen) {
                res = s.substring(l, r + 1)
                resLen = r - l + 1
            }
            l -= 1
            r += 1
        }
    }
    return res
};
```

## Reference

- [https://leetcode.com/problems/longest-palindromic-substring/](https://leetcode.com/problems/longest-palindromic-substring/)