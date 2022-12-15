---
title: 'mysqldump throws: Unknown table 'COLUMN_STATISTICS' in information_schema (1109)'
published: true
tags: MySQL
---

This is due to a new flag that is enabled by default in **mysqldump 8**. You
can disable it by adding `--column-statistics=0`. The command will be
something like:

```shell
mysqldump --column-statistics=0 --host=<server> --user=<user> --password=<password> 
```

To disable column statistics by default, you can add

```bash
[mysqldump]
column-statistics=0
```

to a MySQL config file, go to `/etc/my.cnf`, `~/.my.cnf`, or directly to `/etc/mysql/mysql.cnf`.

## Reference

- [https://serverfault.com/questions/912162/mysqldump-throws-unknown-table-column-statistics-in-information-schema-1109](https://serverfault.com/questions/912162/mysqldump-throws-unknown-table-column-statistics-in-information-schema-1109)