---
title: 'Data Partitioning'
published: true
tags: SystemDesign
---

Data partitioning is a technique to break a big database into many smaller
parts.

## 1. Partitioning Methods

- Horizontal Partitioning:
  - range-based partitioning. If the value whose range is used for
    Partitioning isn't chosen carefully, then the partitioning scheme will
    lead to unbalanced servers.
- Vertical Partitioning:
  - We divide our data to store tables related a specific feature in their own server.
- Directory-Based Partitioning:
  - Create a lookup service that knows current partitioning scheme and
    abstracts it away from the DB access code. So, to find out where a
    particular data entity resides, we query the directory server that holds
    the mapping between each tuple key to its DB server. This loosely coupled
    approach means we can perform tasks like adding servers to the DB pools or
    changing our partitioning scheme without having an impact on the
    application.
 
## 2. Partitioning Criteria

- Key or hash-based Partitioning:
  - Apply a hash function to some key attributes of entity we are storing;
- List partitioning:
  - Each partition is assigned a list of values, so whenever we want to insert
    a new record, we will see which partition contains our key and then store
    it here.
- Round-robin partitioning:
  - With `n` partitions, the `i` tuple is assigned to partition `i mod n`
- Composite Partitioning

## 3. Common Problems of Data Partitioning

- a. Joins and Denormalization
  - Joining across multiple machines will not be performance efficient. A
    common workaround for this problem is to denormalize the database so that
    queries that previously required joins can be performed from a single
    table.
- b. Referential Integrity
  - Applications that require referential integrity have to enforce it in
    application code.
- c. Rebalancing
  - The data distribution is not uniform, there is a lot of load on a partition.
