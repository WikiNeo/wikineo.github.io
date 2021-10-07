---
title: "[LeetCode 3] Longest Substring Without Repeating Characters"
published: true
tags: Algorithm
---

## Problem

Given a string `s`, find the length of the **longest substring** without
repeating characters.

## Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

## Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

## Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a
substring.

## Example 4:

Input: s = ""
Output: 0

## Constraints:

- `0 <= s.length <= 5 * 104`
- `s` consists of English letters, digits, symbols and spaces.

## Thoughts

- As usual, hash can help in array problem.
- Sliding window can help in array/string problem

## Code

```typescript
function lengthOfLongestSubstring(s: string): number {
    let res = 0;
    let valueToIndex = {};
    let leftIndex = 0;
    
    if(s.length < 2) {
        return s.length;
    }
    
    for(let rightIndex = 0; rightIndex < s.length; rightIndex++) {
        let char = s[rightIndex];
        
        if(char in valueToIndex) { 
            // if we find a duplicate, update leftIndex value
	    // The max here deals with case "abba"
            leftIndex = Math.max(valueToIndex[char] + 1, leftIndex);
        } 
	// we need keep updating the mapping and res
        valueToIndex[char] = rightIndex;
        res = Math.max(res, rightIndex - leftIndex + 1)
        
    }
    return res;
};
```

## Reference

- [https://leetcode.com/problems/longest-substring-without-repeating-characters/](https://leetcode.com/problems/longest-substring-without-repeating-characters/)