---
title: "[LeetCode 4] Median of Two Sorted Arrays"
published: true
tags: Algorithm
---

## Problem

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

### Example 1:

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

### Example 2:

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

### Example 3:

```
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
```

### Example 4:

```
Input: nums1 = [], nums2 = [1]
Output: 1.00000
```

### Example 5:

```
Input: nums1 = [2], nums2 = []
Output: 2.00000
```
 
### Constraints:

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-106 <= nums1[i], nums2[i] <= 106`

## Thoughts

- When we see `O(log(m + n))`, think of binary search thing
- The code needs handle the parity of `m + n`
- We could find the correct subarray in `nums1` and `nums2` for the final median
- More cases to consider
  - [1, 2, 4, 5, 5, 6, 7, 8], [1, 2, 6, 9 10]
  - [1, 3, 3, 5, 5, 6, 7, 8], [1, 2, 2, 2, 5]
  - [1, 2, 3, 5, 5, 6, 7], [1, 2, 2, 2 5]

## Code

### Typescript

```typescript
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    // let nums1 be the shorter array
    if (nums2.length < nums1.length) {
        [nums1, nums2] = [nums2, nums1]
    }
    // get total length
    const totalLength = nums1.length + nums2.length;
    // we need the floor function here to get integer index
    const half = Math.floor(totalLength / 2);
    
    // get nums1 leftIndex, rightIndex, medianIndex
    let leftIndex = 0
    let rightIndex = nums1.length - 1
    let medianIndex, medianIndex2
    
    while(true) {
        // floor again for integer
        medianIndex = Math.floor((rightIndex + leftIndex)/2.0)
        // the median for nums2
        medianIndex2 = half - medianIndex - 2
        
        // note the -Number.MAX_VALUE for edge case
        let nums1LeftMax = (medianIndex >= 0) ? nums1[medianIndex] : -Number.MAX_VALUE;
        let nums1RightMin = (medianIndex + 1) < nums1.length ? nums1[medianIndex + 1] : Number.MAX_VALUE;
        let nums2LeftMax = (medianIndex2 >= 0) ? nums2[medianIndex2] : -Number.MAX_VALUE;
        let nums2RightMin = (medianIndex2 + 1 < nums2.length) ? nums2[medianIndex2 + 1] : Number.MAX_VALUE;
        
        // we find the correct interval
        if(nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin) {
            // odd length
            if(totalLength % 2) {
                return Math.min(nums1RightMin, nums2RightMin)
            } else {
                return (Math.max(nums1LeftMax, nums2LeftMax) + Math.min(nums1RightMin, nums2RightMin)) / 2
            }
        } else if(nums1LeftMax > nums2RightMin) {   // we need shrink the subarray
            rightIndex = medianIndex - 1
        } else if(nums2LeftMax > nums1RightMin){    // we need to extend the subarray
            leftIndex = medianIndex + 1
        }
    }
};
```

## Reference

- [https://leetcode.com/problems/median-of-two-sorted-arrays/](https://leetcode.com/problems/median-of-two-sorted-arrays/)