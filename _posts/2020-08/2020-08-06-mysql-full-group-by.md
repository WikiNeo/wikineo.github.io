---
title: "MySQL Full Group By"
published: true
tags: MySQL
---

## my.cnf

```bash
[mysqld]
sql_mode = STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
```

```mysql
set global sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
```

## References

- [Error related to only_full_group_by when executing a query in MySql](https://stackoverflow.com/questions/34115174/error-related-to-only-full-group-by-when-executing-a-query-in-mysql)
