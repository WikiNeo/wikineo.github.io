---
title: 'InnoDB vs MyISAM'
published: true
tags: MySQL
---

## Locking

InnoDB has row-level locking, MyISAM can only do full table-level locking

## Crash Recovery

InnoDB has better crash recovery

## Index

MyISAM has `FULLTEXT` search indexes, InnoDB did not until MySQL 5.6 (Feb 2013)

## Transaction

InnoDB implements transactions, foreign keys and relationship constraints,
MyISAM does not.

## Reference

- [What are the main differences between InnoDB and MyISAM?](https://dba.stackexchange.com/questions/1/what-are-the-main-differences-between-innodb-and-myisam)