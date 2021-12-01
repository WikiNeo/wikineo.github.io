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

## Typescript

```typescript
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    // special case, both empty
    if(!(list1 || list2)) return list1;

    // final list head, we will modify it
    let list = new ListNode();
    // dummy head, it will point list head once
    const dummy = new ListNode();
    // flag for the one time only point
    let flag = true;

    while(list1 || list2) {
        // if both not empty, point list.next to a new node with the value, and go to next
        if(list1 && list2) {
            if(list1.val < list2.val) {
                list.next = new ListNode(list1.val)
                list1 = list1.next;
            } else {
                list.next = new ListNode(list2.val)
                list2 = list2.next;
            }
        } else if(list1) {
            // point the non empty list, and go to next
            list.next = new ListNode(list1.val)
            list1 = list1.next
        } else {
            // point the non empty list, and go to next
            list.next = new ListNode(list2.val)
            list2 = list2.next
        }

        // if it is the first time, point dummy to head
        if(flag) {
            dummy.next = list;
            flag = false;
        }
        // move final list to next
        list = list.next;
    }

    // return final list head
    return dummy.next.next;
};
```

## Reference

- [https://leetcode.com/problems/merge-two-sorted-lists/](https://leetcode.com/problems/merge-two-sorted-lists/)