---
title: 'What is ZooKeeper & How Does it Support Kafka?'
published: true
tags: Kafka
---

ZooKeeper is used in distributed systems for service synchronization and as a
naming registry. When working with Apache Kafka, ZooKeeper is primarily used to
track the status of nodes in the Kafka cluster and maintain a list of Kafka
topics and messages.

## ZooKeeper and Kafka

ZooKeeper has five primary functions. Specially, ZooKeeper is used for
controller election, cluster membership, topic configuration, access control
lists, and quotas.

**#1. Controller Election.** The controller is the broker responsible for
maintaining the leader/follower relationship for all partitions. If ever a node
shuts down, ZooKeeper ensures that other replicas take up the role or partition
leaders replacing the partition leaders in the node that is shutting down.

**#2 Cluster Membership.** ZooKeeper keeps a list of all functioning brokers in
the cluster.

**#3 Topic Configuration.** ZooKeeper maintains the configuration of all topics,
including the list of existing topics, number of partitions for each topic,
location of the replicas, configuration overrides for topics, preferred leader
node, among other details.

**#4 Access Control Lists (ACLs).** ZooKeeper also maintains the ACLs for all
topics. This includes who or what is allowed to read/write to the topic, list of
consumer groups, members of the groups, and the most recent offset each consumer
group received from each partition.

**#5 Quotas.** ZooKeeper accesses how much data each client is allowed to
read/write.

## Reference

- [https://dattell.com/data-architecture-blog/what-is-zookeeper-how-does-it-support-kafka/](https://dattell.com/data-architecture-blog/what-is-zookeeper-how-does-it-support-kafka/)