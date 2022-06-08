---
title: '[LeetCode 424] Longest Repeating Character Replacement'
published: true
tags: TwoPointers
---

## Problem

You are given a string `s` and an integer `k`. You can choose any character of the
string and change it to any other uppercase English character. You can perform
this operation at most `k` times.

Return the length of the longest substring containing the same letter you can
get after performing the above operations.

### Example 1:

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

### Example 2:

```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```

#### Constraints:

- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

## Thoughts

- We can have two pointers to process the substring, for each substring, we
  keep tracking of the `maxCount` of a character, if the length of the
  substring minus the `maxCount` is less than or equal to `k`, we can update
  the result. Otherwise, we decrease the count of `left` character, and move
  it to the right by 1

## TypeScript

```typescript
function characterReplacement(s: string, k: number): number {
    const LEN: number = s.length;
    let res: number = 0;
    let charToCount: Map<string, number> = new Map<string, number>();
    let maxCount: number = 0;
    let left: number = 0;
    
    for(let right = 0; right < LEN; right++){
        let rCount = charToCount.get(s[right]) || 0
        rCount++;
        charToCount.set(s[right], rCount)
        maxCount = Math.max(maxCount, rCount)
        const toReplace: number = right - left + 1 - maxCount
        if(toReplace <= k) {
            res = Math.max(res, right - left + 1)
        } else {
            let lCount = charToCount.get(s[left])
            lCount--
            charToCount.set(s[left], lCount)
            left++
        }
        
    }
    
    return res;
};
```

## Reference

- [https://leetcode.com/problems/longest-repeating-character-replacementhttps://leetcode.com/problems/longest-repeating-character-replacement//]()