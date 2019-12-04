---
title: "Reverse Linked List"
published: true
---

Reverse a singly linked list.

```bash
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

## Thoughts

1. We can keep two pointers `prev` and `cur`
2. Use `tempNext` as a temporary storage

## Code

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

- [https://leetcode-cn.com/problems/reverse-linked-list/](https://leetcode-cn.com/problems/reverse-linked-list/)
