---
title: '[LeetCode 387] First Unique Character in a String'
published: true
tags: Map
---

## Problem

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

### Example 1:

```
Input: s = "leetcode"
Output: 0
```

### Example 2:

```
Input: s = "loveleetcode"
Output: 2
```

### Example 3:

```
Input: s = "aabb"
Output: -1
```

#### Constraints:

- `1 <= s.length <= 105`
- `s` consists of only lowercase English letters.

## Thoughts

- Map with character to count
- Find index of the first character with count === 1

## TypeScript

```typescript
function firstUniqChar(s: string): number {
    const charToCount: Map<string, number> = new Map<string, number>();
    
    s.split('').reduce((acc, c) => {
        if(acc.has(c)){
            acc.set(c, acc.get(c) + 1);
        } else {
            acc.set(c, 1);
        }
        
        return acc;
    }, charToCount)
    

    for(let i = 0; i < s.length; i++){
        if(charToCount.get(s[i]) === 1)
            return i;
    }
    
    return -1;
};
```

## Reference

- [https://leetcode.com/problems/first-unique-character-in-a-string/](https://leetcode.com/problems/first-unique-character-in-a-string/)