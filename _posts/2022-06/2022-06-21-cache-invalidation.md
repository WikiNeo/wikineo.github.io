---
title: 'Cache Invalidation'
published: true
tags: SystemDesign
---

When data is updated in the database, then that data has to be refreshed in the cache as well. This is called cache invalidation.

There are three main methods of cache invalidation

- Write-through cache - Data is written to the cache and database at the same time.

- Write-around cache - Data is written to the database writing to cache. Data is written to cache when a request results in a 'cache miss', at which point data in retrieved from database, written to cache, and send back to client.

- Write-back (Write-behind) cache - Data is written to the cache without writing to database. Data is written to database asynchronously.

## Reference

- [https://www.interviewgrid.com/interview_questions/system_design/caching](https://www.interviewgrid.com/interview_questions/system_design/caching)