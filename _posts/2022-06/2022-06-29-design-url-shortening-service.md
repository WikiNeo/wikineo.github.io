---
title: 'Design a URL Shortening Service Like TinyURL'
published: true
tags: SystemDesign
---

## 1. Why do we need URL shortening?

URL shortening is used to create shorter aliases for long URLs. Users are
redirected to the original URL when they hit these short links.

## 2. Requirements and Goals of the System

### Functional Requirements

1. Given a URL, our service should generate a shorter and unique alias of it.
2. When users access a short link, our service should redirect them to the
   original link.
3. Users should optionally be able to pick a custom short link for their URL.
4. Links will expire after a standard default timespan. Users should be able
   to specify the expiration time.

### Non-Functional Requirements

1. The system should be highly available. This is required because, if our
   service is down, all the URL redirection will start failing.
2. URL redirection should happen in real-time with minimal latency.
3. Shortened links should not be guessable (not predictable).

### Extended Requirements

1. Analytics: e.g., how many times a redirection happened?
2. Our service should also be accessible through REST APIs by other services.

## 3. Capacity Estimation and Constraints

Our system will be read-heavy. There will be lots of redirection requests
compared to new URL shortenings. Let's assume a 100:1 ratio between read and
write.

Estimations:

- Traffic
- Storage
- Bandwidth
- Memory
- High-level

## 4. System APIs

```typescript
createURL(api_dev_key, original_url, custom_alias=null, user_name=null, expire_date=null)
deleteURL(api_dev_key, url_key)
```

## 5. Database Design

A few observations about the nature of the data we will store

1. We need to store billions of records.
2. Each object we store is small (less than 1k)
3. There are no relationships between records - other than storing which user
   created a URL.
4. our service is read-heavy.

Since we are anticipate storing billions of rows, and we don't need to use
relationships between objects - a NoSQL store like DynamoDB, Cassandra is a
better choice. A NoSQL choice would also be easier to scale.

## 6. Basic System Design and Algorithm

- a. Encoding Actual URL
- b. Generating Keys Offline

## 7. Data Partitioning and Replication

- a. Range Based Partition
- b. Hash Based Partitioning
- c. Consistent Hashing

## 8. Cache

- a. How much cache memory should be use?
- b. Which cache eviction policy would be best fit our needs?
- c. How each cache replica be updated?

## 9. Load Balancer

1. between clients and application servers
2. between application servers and database servers
3. between application servers and cache servers.

## 10. Purging or DB cleanup

## 11. Telemetry

## 12. Security and Permissions
