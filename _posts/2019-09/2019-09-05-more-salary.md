---
title: "[LeetCode 181] Employees Earning More Than Their Managers"
published: true
tags: MySQL
---

The `Employee` table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

```SQL
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
```

Given the `Employee` table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

```SQL
+----------+
| Employee |
+----------+
| Joe      |
+----------+
```

## Thoughts

1. We can join a table to itself

## Code

```SQL
SELECT 
    employee.Name AS Employee 
FROM Employee as employee 
    JOIN Employee as manager 
        ON employee.ManagerId = manager.Id AND employee.Salary > manager.Salary;
```

## References

- [https://leetcode.com/problems/employees-earning-more-than-their-managers/](https://leetcode.com/problems/employees-earning-more-than-their-managers/)
