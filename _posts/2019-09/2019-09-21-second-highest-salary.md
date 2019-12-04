---
title: "Second Highest Salary"
published: true
---

Write a SQL query to get the second highest salary from the Employee table.

```SQL
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```

For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

```SQL
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```

## Thoughts

1. Second Highest => `ORDER BY Salary LIMIT 1 OFFSET 1`
2. No Second Highest => `IFNULL( res , NULL)`
3. Consider duplicates

## Code

```SQL
SELECT (
    IFNULL ((SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1), NULL)
) AS SecondHighestSalary;
```

References: [https://leetcode-cn.com/problems/second-highest-salary/](https://leetcode-cn.com/problems/second-highest-salary/)
