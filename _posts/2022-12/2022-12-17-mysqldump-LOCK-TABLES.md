---
title: "mysqldump: Got error: 1044: Access denied for user 'username'@'localhost' to database 'databasename' when using LOCK TABLES"
published: true
tags: MySQL
---

either:

1. your user is missing the `LOCK` privilege, so you should ask your database administrator to grant it to you
2. run the same `mysqldump` command, simply adding the `--single-transaction` flag, eg. `mysqldump --single-transaction -u user -p ...`

## Reference

- [https://dba.stackexchange.com/questions/86991/mysqldump-got-error-1044-access-denied-for-user-usernamelocalhost-to-dat](https://dba.stackexchange.com/questions/86991/mysqldump-got-error-1044-access-denied-for-user-usernamelocalhost-to-dat)