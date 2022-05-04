---
title: '[LeetCode 179] Largest Number'
published: true
tags: String
---

## Problem

Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of
an integer.

### Example 1:

```
Input: nums = [10,2]
Output: "210"
```

### Example 2:

```
Input: nums = [3,30,34,5,9]
Output: "9534330"
```
 
#### Constraints:

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 10^9`

## Thoughts

- We need make sure largest digits occupy most significant digits.

## TypeScript

```typescript
function largestNumber(nums: number[]): string {
    let result: string;
    nums.sort((a, b) => {
        let ba: number = parseInt(b.toString() + a.toString());
        let ab: number = parseInt(a.toString() + b.toString());
        return ba - ab;
    });
    result = nums.join('');
    if (result[0] === '0')
        result = '0';
    return result;
};
```

## Reference

- []()