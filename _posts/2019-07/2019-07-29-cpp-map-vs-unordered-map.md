---
title:  "C++ map vs unordered_map"
published: true
categories: tech
tags: C++
---

## std::map

- ordering: increasing order (by default)
- implementation: self balancing tree like Red-Black Tree
- search time: log(n)
- insertion time: log(n) + rebalance
- deletion time: log(n) + rebalance

### Use std::map when

- You need ordered data
- You would have to print/access the data (in sorted order)
- you need predecessor/successor of elements

## std::unordered_map

- ordering: no ordering
- implementation: hash table
- search time: O(1) -> average O(n) -> worst case
- insertion time: same as search
- deletion time: same as search

### Use std::unordered_map when

- You need to keep count of some data (Example - strings) and no ordering is required.
- You need single element access i.e. no traversal.

References: [https://www.geeksforgeeks.org/map-vs-unordered_map-c/](https://www.geeksforgeeks.org/map-vs-unordered_map-c/)
