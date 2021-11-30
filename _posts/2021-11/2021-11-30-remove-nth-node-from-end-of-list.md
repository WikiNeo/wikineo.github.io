---
title: "[LeetCode 19] Remove Nth Node from End of List"
published: true
tags: List
---

## Problem

Given the head of a linked list, remove the nth node from the end of the list and return its head.

### Example 1:

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

### Example 2:

```
Input: head = [1], n = 1
Output: []
```

### Example 3:

```
Input: head = [1,2], n = 1
Output: [1]
```

### Constraints:

```
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz
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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    // create a dummy node pointing to head
    const dummy = new ListNode(0, head)
    
    let left = dummy;
    let right = head;
    
    // make sure the diff between left & right is n + 1
    while(n > 0 && right) {
        right = right.next;
        n--;
    }
    
    // move both right & left to next until right is null
    // then we have left before the nth node from the end
    while(right) {
        left = left.next
        right = right.next
    }
    
    // deletion
    left.next = left.next.next
    
    
    return dummy.next
    
};
```

## Reference

- [https://leetcode.com/problems/remove-nth-node-from-end-of-list/](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)