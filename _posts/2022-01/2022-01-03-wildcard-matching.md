---
title: '[LeetCode 44] Wildcard Matching'
published: true
tags: DynamicProgramming
---

## Problem

Given an input string (`s`) and a pattern (`p`), implement wildcard pattern
matching with support for `'?'` and `'*'` where:

- `'?'` Matches any single character.
- `'*'` Matches any sequence of characters (including the empty sequence).

The matching should cover the **entire** input string (not partial).
 
### Example 1:

```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

### Example 2:

```
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
```

### Example 3:

```
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
```

### Constraints:

- `0 <= s.length, p.length <= 2000`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'?'` or `'*'`.

## Solution

### TypeScript 1

```typescript
function isMatch(s: string, p: string): boolean {
    // table[i][j] indicates if s.slice(0, i) and p.slice(0, j) match
    const table = Array(s.length + 1).fill(null).map(() => Array(p.length + 1).fill(false))
    
    // empty string & pattern match
    table[0][0] = true;
    
    // deals with starting *
    for(let j = 1; j <= p.length; j++){
        if(p[j - 1] === '*') {
            table[0][j] = table[0][j - 1]
        }
    }
    
    for(let i = 1; i <= s.length; i++) {
        for(let j = 1; j <= p.length; j++) {
            // notice the 1-index diff for table & the pattern
            if(p[j - 1] === '*') {
                // we can either treat * as empty string
                // or any sequence
                table[i][j] = table[i][j - 1] || table[i - 1][j]
            } else if(p[j - 1] === '?' || p[j - 1] === s[i - 1]) {
                table[i][j] = table[i - 1][j - 1]
            } else {
                table[i][j] = false
            }
        }
    }
    
    return table[s.length][p.length];
};
```

### TypeScript 2

```typescript
function isMatch(s, p) {
	const sLen = s.length, pLen = p.length;
    // table[i][j] indicates if s.slice(0, s.length - i) and p.slice(0, p.length - j) match
	const dp = Array(s.length + 2).fill(null).map(() => Array(p.length + 2).fill(false))

	dp[sLen][pLen] = true;
	for (let i = sLen; i >= 0; i--){
		for (let j = pLen - 1; j >= 0; j--) {
			if (s[i] === p[j] || p[j] === '?') dp[i][j] = dp[i + 1][j + 1];
			else if (p[j] === '*') dp[i][j] = dp[i][j + 1] || dp[i + 1][j] || dp[i + 1][j + 1];
		}
	}

	return dp[0][0];
};
```

### Javascript 1

```javascript
var isMatch = function(s, p) {
    p = p.replace(/\*+/g, '*');
    const pCharLen = p.replace(/\*+/g, '').length;
    const sLen = s.length;
    const pLen = p.length;
    if(!sLen) return !pCharLen 
    
    const memo = new Map()
    
    function run(si, pi, pLeft) {
        if(si === sLen && pi === pLen) return true;
        if(sLen - si < pLeft || pi === pLen) return false;
        
        const key = `${si}-${pi}`
        if(memo.has(key)) return memo.get(key)
        
        let res = false;
        
        if(p[pi] === '?' || p[pi] === s[si]) res = run(si+1, pi+1, pLeft-1)
        else if(p[pi] === '*') res = run(si+1, pi, pLeft) || run(si, pi+1, pLeft)

        memo.set(key, res)
        return res;
    }
    return run(0, 0, pCharLen)
};
```

## Reference

- [https://leetcode.com/problems/wildcard-matching/](https://leetcode.com/problems/wildcard-matching/)