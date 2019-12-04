---
title: "Delete Duplicate Emails"
published: true
---

Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

```SQL
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
```

For example, after running your query, the above Person table should have the following
rows:

```SQL
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
```

## Thoughts

1. Use `DELETE`

## Code

```SQL
DELETE p1 FROM Person p1, Person p2
    WHERE p1.Email = p2.Email AND p1.Id > p2.Id;
```

References: [https://leetcode-cn.com/problems/delete-duplicate-emails/](https://leetcode-cn.com/problems/delete-duplicate-emails/)
