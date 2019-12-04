---
title:  "Dijkstra's Shortest Path Algorithm"
published: false
categories: tech
tags: Algorithm
---

Given a graph and a source vertex in the graph, find shortest paths from source to all
vertices in the given graph.

Dijkstra's algorithm is very similar to Prim's algorithm for minimum spanning tree. Like
Prim's MST, we generate a SPT (shortest path tree) with given source as root. We maintain
two sets, one set contains vertices included in the shortest path tree, other set includes
vertices not yet included in shortest path tree.

References: [https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
