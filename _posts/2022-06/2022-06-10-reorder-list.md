---
title: '[LeetCode 143] Reorder List'
published: true
tags: LinkedList
---

## Problem

You are given the head of a singly linked-list. The list can be represented as:

```
L0 → L1 → … → Ln - 1 → Ln
```

Reorder the list to be on the following form:

```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

### Example 1:

```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

### Example 2:

```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

#### Constraints:

- The number of nodes in the list is in the range `[1, 5 * 10^4]`.
- `1 <= Node.val <= 1000`

## Thoughts

- Use slow & fast pointer to find mid pointer
- Reverse the second part
- Then do merge

## TypeScript

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

/**
 Do not return anything, modify head in-place instead.
 */
function reorderList(head: ListNode | null): void {
    let slow: ListNode = head, fast: ListNode = head.next;
    
    // move slow to the mid
    while(fast && fast.next){
        slow = slow.next
        fast = fast.next.next
    }

    // reverse the second part
    let second: ListNode = slow.next;
    // end first
    slow.next = null
    let prev: ListNode = null
    while(second){
        const temp: ListNode = second.next
        second.next = prev
        prev = second;
        second = temp;
    }

    // merge now
    let first: ListNode = head;
    second = prev;

    while(second){
        const temp1: ListNode = first.next;
        const temp2: ListNode = second.next;
        first.next = second
        second.next = temp1;
        first = temp1
        second = temp2
    }
};
```

## Reference

- [https://leetcode.com/problems/reorder-list/](https://leetcode.com/problems/reorder-list/)