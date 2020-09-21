---
title:  "Breadth-First Search"
published: true
tags: Algorithm
---

**Breadth-first search (BFS)** is an algorithm for traversing or searching tree or graph
data structure. It starts at the tree root (or some arbitrary node of a graph, sometimes
referred to as a 'search key'), and explores all of the neighbor nodes at the present
depth prior to moving on to the nodes at the next depth level.

## Pesudocode

Input: A graph *Graph* and a *starting vertex root* of *Graph*

```ruby
def BFS(G, start_v):
    let Q be a queue
    label start_v as discovered
    Q.enqueue(start_v)
    while Q is not empty
        v = Q.dequeue()
        if v is the goal:
            return v
        for all edges from v to w in G.adjacentEdges(v) do
            if w is not labeled as discovered
            w.parent = v
            Q.enqueue(w)
```

### More details

This non-recursive implementation is similar to the recursive implementation of
depath-first search, but differs from it in two ways:

1. it uses a queue (First In First Out) instead of a stack
2. it checks whether a vertex has been discovered before enqueueing the vertex rather than
   delaying this check until the vertex is dequeued from the queue.

The Q queue contains the frontier along which the algorithm is currently searching.

Nodes can be labelled as discovered by storing them in a set, or by an attribute on each
node, depending on the implementation.

Note that the word *node* is usually interchangeable with the word *vertex*.
