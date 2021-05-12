---
title: "[LeetCode 197] Rising Temperature"
published: true
tags: MySQL
---

Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

```SQL
+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
```

For example, return the following Ids for the above Weather table:

```SQL
+----+
| Id |
+----+
|  2 |
|  4 |
+----+
```

## Thoughts

1. For relation within a single table, we can join with itself
2. DATEDIFF() can be used.

## Code

```SQL
SELECT
    w2.Id 
FROM Weather as w1 
    JOIN Weather as w2 ON DATEDIFF(w2.RecordDate, w1.RecordDate) = 1 AND w2.Temperature > w1.Temperature;
```

## References

- [https://leetcode.com/problems/rising-temperature/](https://leetcode.com/problems/rising-temperature/)
