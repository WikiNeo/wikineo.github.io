---
title: '[LeetCode 76] Minimum Window Substring'
published: true
tags: TwoPointers
---

## Problem

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum
window substring** of `s` such that every character in `t` (**including duplicates**) is
included in the window. If there is no such substring, return the empty string
`""`.

The testcases will be generated such that the answer is **unique**.

A **substring** is a contiguous sequence of characters within the string.

### Example 1:

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

### Example 2:

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

### Example 3:

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

### Constraints:

```
- m == s.length
- n == t.length
- 1 <= m, n <= 105
- s and t consist of uppercase and lowercase English letters.
```

### Follow up: 

- Could you find an algorithm that runs in `O(m + n)` time?

## TypeScript

```TypeScript
function minWindow(s: string, t: string): string {
    // special case
    if(t === "") return "";
    
    // have two hash to store number of characters
    const countS: {[index: string]: number} = {};
    const countT: {[index: string]: number} = {};
    
    // initialize countT
    for(let c of t){
        countT[c] = (c in countT) ? (countT[c] + 1) : 0
    }
    
    // if we have what we need, counting if each character has met the condition
    let have: number = 0;
    const need: number = Object.keys(countT).length;
    
    // result, and its length
    let resultL: number = -1, resultR: number = -1, resultLen: number = Infinity;
    
    let l: number = 0;
    
    // let's iterate through s and do our update
    for(let r = 0; r < s.length; r++){
        const c: string = s[r]
        
        // update character count in countS
        countS[c] = (c in countS) ? (countS[c] + 1) : 0;
        
        // update our have count
        if(c in countT && countS[c] === countT[c]){
            have++
        }
        
        // we will update result & shrink the result string while the have === need
        while(have === need){
            // update result
            if(r - l + 1 < resultLen){
                resultL = l;
                resultR = r;
                resultLen = r - l + 1;
            }
            // shrink window
            countS[s[l]]--;
            // update have
            if(s[l] in countT && countS[s[l]] < countT[s[l]]){
                have--;
            }
            l++
        }
    }
    
    if(resultLen === Infinity){
        return ''
    } else {
        return s.slice(resultL, resultR + 1)
    }
    
};
```

## Reference

- [https://leetcode.com/problems/minimum-window-substring/](https://leetcode.com/problems/minimum-window-substring/)