---
title: '[LeetCode 131] Palindrome Partitioning'
published: true
tags: Backtracking
---

## Problem

Given a string `s`, partition `s` such that every substring of the partition
is a **palindrome**. Return all possible palindrome partitioning of `s`.

A **palindrome** string is a string that reads the same backward as forward.
 
### Example 1:

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

### Example 2:

```
Input: s = "a"
Output: [["a"]]
```
 
#### Constraints:

- 1 <= s.length <= 16
- s contains only lowercase English letters.

## TypeScript

```typescript
function partition(s: string): string[][] {
    let res: string[][] = [];
    let part: string[] = [];
    
    const isPalindrome = (str: string, left: number, right: number): boolean => {
             
        while(left < right){
            if(str[left] !== str[right]){
                return false;
            }
            left++;
            right--;
        }
            
        return true;
    }
    
    const dfs = (i: number): void => {
        if(i >= s.length){
            res.push([...part])
            return
        }
        
        for(let j = i; j < s.length; j++){
            if(isPalindrome(s, i, j)){
                part.push(s.substring(i, j + 1));
                dfs(j + 1)
                part.pop()
            }
        }
    
        
    }
    dfs(0)
    
    return res;
};
```

## Reference

- [https://leetcode.com/problems/palindrome-partitioning/](https://leetcode.com/problems/palindrome-partitioning/)