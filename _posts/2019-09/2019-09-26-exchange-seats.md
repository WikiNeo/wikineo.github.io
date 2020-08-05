---
title: "Exchange Seats"
published: true
tags: MySQL
---

Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.
 
Mary wants to change seats for the adjacent students.
 
Can you write a SQL query to output the result for Mary?

```SQL
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
```

For the sample input,the output is

```SQL
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
```

If the number of students is odd, there is no need to change the last one's seat.

## Thoughts

1. Since we try to output something, we will use `SELECT`
2. Since we are changing output based on different pattern, we will use `CASE`
3. The last element is the one with maximum id, we can get the value with `SELECT MAX(id)
   FROM seat`

### Simple CASE Expression

The following illustrates the syntax ofa simple `CASE` expression:

```SQL
CASE value
    WHEN value1 THEN result1
    WHEN value2 THEN result2
    ...
    [ELSE else_result]
END
```

The `CASE` compares the `value` with `values` in the `WHEN` clauses for equality, you
cannot use it with `NULL` because `NULL = NULL` returns false.

### Searched CASE Expression

The following shows the syntax of a searched `CASE` expression:

```SQL
CASE
    WHEN expression1 THEN result1
    WHEN expression2 THEN result2
    ...
    [ELSE else_result]
END
```

## Code

```SQL
SELECT (CASE
    WHEN id%2 = 0 THEN id - 1
    WHEN id = (SELECT max(id) FROM seat) THEN id
    ELSE id + 1
    END) as id, student
FROM seat ORDER BY id;
```

## References

- [https://leetcode-cn.com/problems/exchange-seats/](https://leetcode-cn.com/problems/exchange-seats/)
- [http://www.mysqltutorial.org/mysql-case-function/](http://www.mysqltutorial.org/mysql-case-function/)
