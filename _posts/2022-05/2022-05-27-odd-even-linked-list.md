---
title: '[LeetCode 289] Odd Even Linked List'
published: true
tags: LinkedList
---

## Problem

Given the `head` of a singly linked list, group all the nodes with odd indices
together followed by the nodes with even indices, and return the reordered
list.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

### Example 1:

```
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
```

### Example 2:

```
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
```
 
#### Constraints:

- The number of nodes in the linked list is in the range `[0, 10^4]`.
- `-10^6 <= Node.val <= 10^6`

## Thoughts

- Try with 3 & 4 node first
- Handle special case

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

function oddEvenList(head: ListNode | null): ListNode | null {
    if(head === null || head.next === null || head.next.next === null){
        return head;
    }
    
    let h1: ListNode = head;
    let h2: ListNode = head.next;
    const dummy: ListNode = h2;
    
    while(h2 && h2.next){
        h1.next = h2.next;
        h1 = h1.next;
        h2.next = h1.next
        h2 = h2.next;
    }
    h1.next = dummy;
    
    return head;
};
```

## Reference

- [https://leetcode.com/problems/odd-even-linked-list/](https://leetcode.com/problems/odd-even-linked-list/)