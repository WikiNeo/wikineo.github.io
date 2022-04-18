---
title: '[LeetCode 140] Word Break II'
published: true
tags: DynamicProgramming
---

## Problem

Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in **any order**.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

### Example 1:

```
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
```

### Example 2:

```
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
```

### Example 3:

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
```
 
#### Constraints:

- `1 <= s.length <= 20`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 10`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are **unique**.

## TypeScript

```typescript
function wordBreak(s: string, wordDict: string[]): string[] {
    const LEN = s.length;
    const table: string[][][] = new Array(LEN + 1).fill([]).map(x => []);
    table[LEN].push([''])
    
    for(let i = LEN - 1; i >= 0; i--){
        for(const word of wordDict){
            const WORD_LEN = word.length
            if((i + WORD_LEN) <= LEN && s.substring(i, i + WORD_LEN) === word){
                const temp: string[][] = table[i + WORD_LEN].map(x => [word, ...x]);
                table[i].push(...temp);
            }
        }
    }
    
    
    return table[0].map(x => x.filter(c => c !== '').join(' '))

};
```

## Reference

- [https://leetcode.com/problems/word-break-ii/](https://leetcode.com/problems/word-break-ii/)