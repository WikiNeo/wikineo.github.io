---
title: '[LeetCode 41] First Missing Positive'
published: true
tags: Set
---

## Problem

Given an unsorted integer array `nums`, return the smallest missing positive integer.

You must implement an algorithm that runs in `O(n)` time and uses constant extra space.

### Example 1:

```
Input: nums = [1,2,0]
Output: 3
```

### Example 2:

```
Input: nums = [3,4,-1,1]
Output: 2
```

### Example 3:

```
Input: nums = [7,8,9,11,12]
Output: 1
```
 
### Constraints:

```
- 1 <= nums.length <= 5 * 105
- -231 <= nums[i] <= 231 - 1
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {

	// update all negative numbers to 0, since they will not affect the final result
	for(let i = 0; i < nums.length; i++){
		if(nums[i] < 0) {
			nums[i] = 0
		}
	}

    // we will mark index i as negative, indicating i + 1 exists in array, thus using the array as Set
	for(let i = 0; i < nums.length; i++) {
		let val = Math.abs(nums[i])
		if(1 <= val && val <= nums.length) {
			if(nums[val - 1] > 0) {
				nums[val - 1] *= -1
			} else if(nums[val - 1] === 0) {
				nums[val - 1] = -1 * (nums.length + 1)
			}
		}
	}

    // in solution set, we loop from the smallest possible value and check for positive or 0 values
	for(let i = 1; i < nums.length + 1; i++) {
		if(nums[i - 1] >= 0) {
			return i
		}
	}

	return nums.length + 1
};
```

## Reference

- [https://leetcode.com/problems/first-missing-positive/](https://leetcode.com/problems/first-missing-positive/)