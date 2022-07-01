---
title: '[LeetCode 242] Valid Anagram'
published: true
tags: Map
---

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 1:

```
Input: s = "anagram", t = "nagaram"
Output: true
```

### Example 2:

```
Input: s = "rat", t = "car"
Output: false
```
 
### Constraints:

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Thoughts

- We can use `Map` to store character to count for the first string
- Then for each character in second string, we decrease the count

## TypeScript

```typescript
function isAnagram(s: string, t: string): boolean {
    if(s.length !== t.length) {
        return false;
    }
    
    const valueToCount: Map<string, number> = new Map<string, number>();
    
    
    for(let c of s){
        const count: number = valueToCount.get(c) || 0
        valueToCount.set(c, count + 1)
    }
    
    for(let c of t){
        const count: number = valueToCount.get(c) || 0
        if(count === 0) {
            return false
        }
        valueToCount.set(c, count - 1)
    }
    
    return true;
};
```

## Reference

- [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/)