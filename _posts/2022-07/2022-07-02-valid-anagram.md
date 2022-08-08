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

## Code

### TypeScript

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

### Ruby

```ruby
# store character to count for first string, then check it with the second
#
# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
  # base case
  return false if s.length != t.length

  char_to_count = {}

  # store character to count for s
  s.chars.each do |char|
    count = char_to_count.key?(char) ? char_to_count[char] : 0
    char_to_count[char] = count + 1
  end

  # check character to count for t
  t.chars.each do |char|
    count = char_to_count.key?(char) ? char_to_count[char] : 0
    # return false if we can't find the char
    return false if count == 0
    # update the hash
    char_to_count[char] = count - 1
  end

  true
end
```

## Reference

- [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/)