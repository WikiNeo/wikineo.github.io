---
title: "[LeetCode 206] Reverse Linked List"
published: true
tags: LinkedList
---

## Problem

Reverse a singly linked list.

```bash
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

## Thoughts

1. We can keep two pointers `prev` and `cur`
2. Use `tempNext` as a temporary storage

## Code

### TypeScript

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

function reverseList(head: ListNode | null): ListNode | null {
    if(head === null || head.next === null) {
        return head;
    }
    
    let left: ListNode = null, right: ListNode = head;
    
    while(right !== null){
        const temp: ListNode = right.next;
        right.next = left;
        left = right;
        right = temp;
    }
    
    return left;
};
```

### C++

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* cur = head;
        while(cur != nullptr){
            // Assign temporary value first
            auto tempNext = cur->next;
            cur->next = prev;
            prev = cur;
            // Assign loop control variable last
            cur = tempNext;
        }
        return prev;
    }
};
```

References:

- [https://leetcode.com/problems/reverse-linked-list/](https://leetcode.com/problems/reverse-linked-list/)
