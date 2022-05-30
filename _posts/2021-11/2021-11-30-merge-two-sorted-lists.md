---
title: "[LeetCode 21] Merge Two Sorted Lists"
published: true
tags: LinkedList
---

## Problem

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

### Example 1:

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

### Example 2:

```
Input: list1 = [], list2 = []
Output: []
```

### Example 3:

```
Input: list1 = [], list2 = [0]
Output: [0]
```
 
### Constraints:

```
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
```

## Thoughts

- Typical merge sort
- Remember to upate head to next

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

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    let head: ListNode = new ListNode();
    const dummy: ListNode = head;
    
    while(list1 && list2){
        if(list1.val <= list2.val){
            head.next = new ListNode(list1.val)
            list1 = list1.next;
        } else {
            head.next = new ListNode(list2.val)
            list2 = list2.next;
        }
        head = head.next
    }
    
    while(list1){
        head.next = new ListNode(list1.val)
        list1 = list1.next
        head = head.next
    }
    
    while(list2){
        head.next = new ListNode(list2.val)
        list2 = list2.next
        head = head.next
    }
    
    return dummy.next;
};
```

## Reference

- [https://leetcode.com/problems/merge-two-sorted-lists/](https://leetcode.com/problems/merge-two-sorted-lists/)