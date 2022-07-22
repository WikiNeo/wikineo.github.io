---
title: 'Designing Instagram'
published: true
tags: SystemDesign
---

## 1. What is Instagram?

Instagram is a social networking service that enables its users to upload and
share their photos and videos with other users. 

## 2. Requirements and Goals of the System

### Functional Requirements

1. Users should be able to upload/download/view photos.
2. Users can perform searches based on photo/video titles.
3. Users can follow other users.
4. The system should generate and display a user's News Feed consisting of top
   photos from all the people the user follows.

### Non-functional Requirements

1. Our service needs to be highly available.
2. The acceptable latency of the system is 200ms for News Feed generation.
3. Consistency can take a hit (in the interest of availability) if a user
   doesn't see a photo for a while; it should be fine
4. The system should be highly reliable; any uploaded photo or video should
   never be lost

## 3. Some Design Considerations

The system would be read-heavy, so we will focus on building a system that can
retrieve photo quickly.

1. Practically, users can upload as many phots as they like; therefore,
   efficient management of storage should be a crucial factor in designing
   this system.
2. Low latency is expected while viewing photos.
3. Data should be 100% reliable. If a user uploads a photo, the system will
   guarantee that it will never be lost.

## 4. Capacity Estimation and Constraints

Calculate total space required with DAU, photo file size

## 5. High Level System Design

At a high-level, we need to support two scenarios, one to upload photos and
the other to view/search photos. Our service would need some object storage
servers to store photos and some database servers to store metadata
information about the photos

## 6. Database Schema

We need to store data about users, their uploaded photos, and the people they
follow.

## 7. Data Size Estimation

Estimate database tables size.

## 8. Component Design

Photo writes can be slow as they have to go to the disk, whereas reads will be
faster, especially they are being served from cache.

Uploading users can consume all the available connections, as uploading is a
slow process. This means that 'reads' cannot be served if the system gets busy
with the 'write' requests. To handle this bottleneck, we can split reads and
writes into separate services. We will have dedicated servers for reads and
different servers for writes to ensure that uploads don't hog the system.

## 9. Reliability and Redundancy

We can run a redundant secondary copy of the service that is not serving any
traffic, but it can take control after the failover when the primary has a
problem.

## 10. Data Sharding

### a. Partitioning based on UserID

We will find the shard number by `UserID % 10`

#### What are the different issues with this partitioning scheme

1. How would we handle hot users?
2. Some users will have a lot of photos compared to others, thus making a
   non-uniform distribution of storage.
3. What if we cannot store all pictures of a user on one shard? If we
   distribute photos of a user onto multiple shards, will it cause higher
   latencies?
4. Storing all photos of a user on one shard can cause issues like
   unavailability of all of the user's data if that shard is down or higher
   latency if it is serving high load.

### b. Partitioning based on PhotoID

#### How can we generate PhotoIDs?

One solution could be that we dedicate a separate database instance to
generate auto-incrementing IDs.

## 11. Rankings and News Feed Generation

### Pre-generating the News Feed

We can have dedicated servers that are continuously generating users' News
Feeds and storing them in a `UserNewsFeed` table.

## 12. News Feed Creation with Sharded Data

One of the most important requirements to create the News Feed for any given
user is to fetch the latest photos from all people the user follows. For this,
we need to have a mechanism to sort photos on their time of creation. To
efficiently do this, we can make photo creation time part of the PhotoID. As
we will have a primary index on PhotoID, it will be quite quick to find the
latest PhotoIDs.

We an use epoch time for this. Let's say our PhotoID will have two parts; the
first part will be representing epoch time, and the second part will be an
auto-incrementing sequence.

## 13. Cache and Load Balancing

- Geographically distributed photo cache servers
- CDN
- Cache for metadata servers
- We can try caching 20% of the daily read volume of photos and metadata.
