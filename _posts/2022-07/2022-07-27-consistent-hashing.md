---
title: 'Consistent Hashing'
published: true
tags: SystemDesign
---

## Background

- Data partitioning
  - It is the process of distributing data across a set of servers. It
    improves the scalability and performance of the system.
- Data replication
  - It is the process of making multiple copies of data and storing them on
    different servers. It improves the availability and durability of the data
    across the system

## What is data partitioning?

There are two challenges when we try to distribute data:

1. How do we know on which node a particular piece of data will be stored?
2. When we add or remove nodes, how do we know what data will be moved from
   exiting nodes to the new nodes? Additionally, how can me minimize data
   movement when nodes join or leave?

## Consistent Hashing to the rescue

Consistent Hashing map data to physical nodes and ensures that only a small
set of keys move when servers are added or removed.

Consistent Hashing stores the data managed by a distributed system in a ring.
Each node in the ring is assigned a range of data.

With consistent hashing, the ring is divided into smaller, predefined ranges.
Each node is assigned one of these ranges. The start of the range is called a
token. This means that each node will be assigned one token. The range
assigned to each node is computed as follows:

- **Range start**: Token value
- **Range end**: Next token value - 1

Whenever the system need to read or write data, the first step it performs is
to apply the MD5 hashing algorithm to the key. The output of this hashing
algorithm determines within which range the data lies and hence, on which node
the data will be stored. 

The Consistent Hashing scheme described above works great when a node is added
or removed from the ring, as in these cases, since only the next node is
affected. For example, when a node is removed, the next node become
responsible for all the keys of the keys stored on the outgoing node. However,
this scheme can result in non-uniform data and load distribution. This problem
can be solved with the help of Virtual nodes.

## Virtual Nodes

Here are a few potential issues associated with a manual and fixed division of
the ranges

- **Adding or removing nodes**: Adding or removing nodes will result in
  recomputing the tokens causing a significant administrative overhead for a
  large cluster.
- **Hotspots**: Since each node is assigned one large range, if the data is
  not evenly distributed, some nodes can be hotspots.
- **Node rebuilding**: Since each node's data might be replicated (for
  fault-tolerance) on a fixed number of other nodes, when we need to rebuild a
  node, only its replica can provide the data. This puts a lot of pressure on
  the replica nodes and can lead to service degradation.

  Instead of assigning a single token to a node, the hash range is divided
  into multiple smaller ranges, and each physical node is assigned several of
  these smaller ranges. Each of these subranges is considered a Vnode. With
  Vnodes, instead of a node being responsible for just one token, it is
  responsible for many tokens (for subranges).

  Practically, Vnodes are randomly distributed across the cluster and are
  generally non-contiguous so that no two neighboring Vnodes are assigned tot
  the same physical node or rack. Additionally, nodes do carry replicas of
  other nodes for fault tolerance. Also, since there can be heterogeneous
  machines in the clusters, some severs might hold more Vnodes than others.
  The figure below shows how physical nodes A, B, C, D, & E use Vnodes of the
  Consistent Hash ring. Each physical node is assigned a set of Vnode and each
  Vnode is replicated once.

## Advantage of Vnodes

1. As Vnodes help spread the load more evenly across the physical nodes on the
   cluster by dividing the hash ranges into smaller sub-ranges, this speeds up
   the rebalancing process after adding or removing nodes. When a new node is
   added, it receives many Vnodes from the existing nodes to maintain a
   balanced cluster. Similarly, when a node needs to be rebuilt, instead of
   getting data from a fixed number of replicas, many node participate in the
   rebuild process.
2. Vnodes make it easier to maintain a cluster containing heterogeneous
   machines. This means, wih Vnodes, we can assign a high number of sub-ranges
   to a powerful server and a lower number of sub-ranges to a less powerful
   server.
3. In contrast to one big range, since Vnodes help assign smaller ranges to
   each physical node, this decreases the probability of hotspots.

## Data replication using Consistent Hashing

To ensure highly availability and durability, Consistent Hashing replicates
each data item on multiple N nodes in the system when the value N is
equivalent to the replication factor.

The replication factor is the number of nodes that will receive the copy of
the same data. For example, a replication factor of two means there are two
copies of each data items, where each copy is stored on a different node.

Each key is assigned to a coordinator node (generally the first node that
falls in the hash range), which first stores the data locally and then
replicates to *N - 1* clockwise successor nodes on the ring. This results in
each node owning the region on the ring between it and its *Nth* predecessor.
In an eventually consistent system, the replication is done asynchronously (in
the background).

In eventually consistent systems, copies of data don't always have to be
identical as long as they are designed to eventually become consistent. In
distributed systems, eventual consistency is used to achieve hight
availability.

## Consistent Hashing use cases

Amazon's Dynamo and Apache Cassandra use Consistent Hashing to distribute and
replicate data across nodes.
