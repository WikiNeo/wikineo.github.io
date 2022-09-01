---
title: 'Priority Queue'
published: true
tags: PriorityQueue
---

In computer science, a **priority queue** is an abstract data-type similar to a
regular queue or stack data structure in which each element additionally has a
*priority* associated with it. In a priority queue, an element with high
priority is served before an element with low priority. In some
implementations, if two elements have the same priority, they are served
according to the order in which they were enqueued; in other implementations
ordering of elements with the same priority remains undefined.

While coders often implement priority queues with heaps, they are conceptually
distinct from heaps. A priority queue is a concept like a list or a map; just
as a list can be implemented with a linked list or with an array, a priority
queue can be implemented with a heap or with a variety of other methods such
as an unordered array.

## Operations

A priority queue must at least support the following operations:

- *is_empty*: check whether the queue has no elements.
- *insert_with_priority*: add an element to the queue with an associated priority.
- *pull_highest_priority_element*: remove the element from the queue that has
  the highest priority, and return it.
	- This is also known as "*pop_element(Off)*", "*get_maximum_element*" or "*get_front(most)_element*".
	- Some conventions reverse the order of priorities, considering lower values to be higher priority, so this may also be known as "*get_minimum_element*", and is often referred to as "*get-min*" in the literature.
	- This may instead be specified as separate "*peek_at_highest_priority_element*" and "*delete_element*" functions, which can be combined to produce "*pull_highest_priority_element*".

In addition, *peek* (in this context often called *find-max* or *find-min*), which returns the highest-priority element but does not modify the queue, is very frequently implemented, and nearly always executes in O(1) time. This operation and its O(1) performance is crucial to many applications of priority queues.

More advanced implementations may support more complicated operations, such as
*pull_lowest_priority_element*, inspecting the first few highest- or
lowest-priority elements, clearing the queue, clearing subsets of the queue,
performing a batch insert, merging two or more queues into one, incrementing
priority of any element, etc.

Stacks and queues are different than priority queues. In a priority queue, the ordering is intrinsic: it depends on the value being inserted. In a stack or queue, the ordering is extrinsic: it depends on the order in which the value is inserted. In terms of behavioral subtyping, a queue is not a subtype of a priority queue, and a priority queue is not a subtype of a queue. Neither one can be substituted for the other, nor should either one be a subtype of the other in an inheritance hierarchy.

## Reference

- [https://en.wikipedia.org/wiki/Priority_queue](https://en.wikipedia.org/wiki/Priority_queue)
