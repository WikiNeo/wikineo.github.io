---
title: '[LeetCode 23] Merge k Sorted Lists'
published: true
tags: LinkedList
---

## Problem

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

### Example 1:

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

### Example 2:

```
Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
```

### Constraints:

```
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length won't exceed 10^4.
```

## Typescript

```typescript
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    // special case handle
    if(lists.length === 0) return null;
    
    const values = []
    
    // save all node values and sort them
    for(let list of lists){
        while(list !== null) {
            values.push(list.val)
            list = list.next
        }
    }
    values.sort((a, b) => a - b)

    // create current & dummy node for iteration
    let cur = new ListNode(0)
    let dummy = cur;
    for(let i = 0; i < values.length; i++){
        cur.next = new ListNode(values[i])
        cur = cur.next
    }

    // return dummy next
    return dummy.next;
};
```

## Reference

- [https://leetcode.com/problems/merge-k-sorted-lists/](https://leetcode.com/problems/merge-k-sorted-lists/)

