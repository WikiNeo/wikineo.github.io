---
title: "[LeetCode 182] Duplicate Emails"
published: true
tags: MySQL
---

Write a SQL query to find all duplicate emails in a table named Person.

```SQL
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
```

For example, your query should return the following for the above table:

```SQL
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
```

## Thoughts

The `GROUP BY` clause groups a set of rows into a set of summary rows by values of columns
or expressions. The `GROUP BY` clause returns one row for each group. In other words, it
reduces the number of rows in the result set.

## Code

```SQL
SELECT Email FROM Person GROUP BY Email HAVING COUNT(Email) > 1;
```

## References

- [https://leetcode.com/problems/duplicate-emails](https://leetcode.com/problems/duplicate-emails)
- [https://www.mysqltutorial.org/mysql-group-by.aspx](https://www.mysqltutorial.org/mysql-group-by.aspx)
