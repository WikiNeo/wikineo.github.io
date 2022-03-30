---
title: '[LeetCode 139] Word Break'
published: true
tags: DynamicProgramming
---

## Problem

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

### Example 1:

```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

### Example 2:

```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```

### Example 3:

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```
 
#### Constraints:

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of wordDict are **unique**.

## TypeScript

```TypeScript
function wordBreak(s: string, wordDict: string[]): boolean {
    const LEN: number = s.length;
    const dp: boolean[] = new Array(LEN + 1).fill(false);
    dp[LEN] = true;
    
    for(let i = LEN - 1; i >= 0; i--){
        for(const word of wordDict){
            const WORD_LEN = word.length;
            if((i + WORD_LEN) <= LEN && s.substring(i, i + WORD_LEN) === word){
                dp[i] = dp[i + WORD_LEN];
            }
            if(dp[i]){
                break;
            }
        }
    }
    
    return dp[0]
};
```

## Reference

- [https://leetcode.com/problems/word-break/](https://leetcode.com/problems/word-break/)