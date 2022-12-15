---
title: 'Access denied; you need (at least one of) the PROCESS privilege(s) for this operation' when trying to dump tablespaces'
published: true
tags: MySQL
---

use `--no-tablespaces`

see mysqldump-Documentation

> mysqldump requires at least the SELECT privilege for dumped tables, SHOW VIEW for dumped views, TRIGGER for dumped triggers, LOCK TABLES if the --single-transaction option is not used, and (as of MySQL 8.0.21) PROCESS if the --no-tablespaces option is not used. Certain options might require other privileges as noted in the option descriptions.

and see documentation of param no-tablespaces

> --no-tablespaces, -y
> This option suppresses all CREATE LOGFILE GROUP and CREATE TABLESPACE statements in the output of mysqldump.

## Reference

- [https://dba.stackexchange.com/questions/271981/access-denied-you-need-at-least-one-of-the-process-privileges-for-this-ope](https://dba.stackexchange.com/questions/271981/access-denied-you-need-at-least-one-of-the-process-privileges-for-this-ope)