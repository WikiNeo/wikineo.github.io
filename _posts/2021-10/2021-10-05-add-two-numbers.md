---
title: "Add Two Numbers"
published: true
tags: Algorithm
---

## Problem

You are given two **non-empty** linked lists representing two **non-negative**
integers. The digits are stored in **reverse order**, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

## Example 1

![Example 1](/../../assets/addtwonumber1.jpg)

```shell
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

## Example 2

```shell
Input: l1 = [0], l2 = [0]
Output: [0]
```

## Example 3

```shell
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

## Constraints

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading
  zeros.

## Thoughts

- A dummy head helps with the single linked list problem
- We can loop two lists until they are all null, note their lengths may be different
- Carry value is used in the current value calculation
- Note there may be ending extra carry

## Code

### Typescript

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

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let dummyHead = new ListNode(0);
    let cur = dummyHead;
    let l1Val, l2Val, tempVal, curVal, carry = 0;
    
    while(l1 !== null || l2 !== null) {    
        // handle null node value access
        l1Val = l1 === null ? 0 : l1.val;
        l2Val = l2 === null ? 0 : l2.val;
        // calculate value with the carry
        tempVal = l1Val + l2Val + carry;
        carry = tempVal >= 10 ? 1 : 0;
        curVal = carry ? tempVal - 10 : tempVal
        cur.next = new ListNode(curVal);
        cur = cur.next;
        
        // go to next node if possible
        l1 = l1 === null ? l1 : l1.next;
        l2 = l2 === null ? l2 : l2.next;
    }

    // don't forget the ending carry
    if(carry) {
        cur.next = new ListNode(1)
    }
    
    return dummyHead.next;
};
```

## Reference

- [https://leetcode.com/problems/add-two-numbers/](https://leetcode.com/problems/add-two-numbers/)
