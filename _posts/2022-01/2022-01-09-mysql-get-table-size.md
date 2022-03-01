---
title: 'Get table size in MySQL'
published: true
tags: MySQL
---

Like most relational databases, MySQL provides useful metadata about the
database itself. While most other databases refer to this information as a
`catalog`, the official MySQL documentation refers to the `INFORMATION_SCHEMA`
metadata as `tables`.

## List Table Sizes From a Single Database

- `DATA_LENGTH` is the length (or size) of all data in the table (in bytes).
- `INDEX_LENGTH` is the length (or size) of the index file for the table (also
  in bytes).

### Size of All Tables

```SQL
SELECT
  TABLE_NAME AS `Table`,
  ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024) AS `Size (MB)`
FROM
  information_schema.TABLES
WHERE
  TABLE_SCHEMA = "bookstore"
ORDER BY
  (DATA_LENGTH + INDEX_LENGTH)
DESC;
```

```
+----------------------------------+-----------+
| Table                            | Size (MB) |
+----------------------------------+-----------+
| book                             |       267 |
| author                           |        39 |
| post                             |        27 |
| cache                            |        24 |
```

### Size of A Single Table

```SQL
SELECT
  TABLE_NAME AS `Table`,
  ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024) AS `Size (MB)`
FROM
  information_schema.TABLES
WHERE
    TABLE_SCHEMA = "bookstore"
  AND
    TABLE_NAME = "book"
ORDER BY
  (DATA_LENGTH + INDEX_LENGTH)
DESC;
```

```
+-------+-----------+
| Table | Size (MB) |
+-------+-----------+
| book  |       267 |
+-------+-----------+
1 row in set (0.00 sec)
```

## List All Table Sizes From ALL Databases

```SQL
SELECT
  TABLE_SCHEMA AS `Database`,
  TABLE_NAME AS `Table`,
  ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024) AS `Size (MB)`
FROM
  information_schema.TABLES
ORDER BY
  (DATA_LENGTH + INDEX_LENGTH)
DESC;
```

## Reference

- [https://chartio.com/resources/tutorials/how-to-get-the-size-of-a-table-in-mysql/](https://chartio.com/resources/tutorials/how-to-get-the-size-of-a-table-in-mysql/)