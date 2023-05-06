---
title: "Delete Rows with Duplicated Column Value in SQLite"
published: true
tags: SQLite
---

## Problem

|id|word|created_at|
|--|--|--|
|1|hello|2023-05-05 10:12:13|
|2|hello|2023-05-05 10:12:13|
|3|hello|2023-05-05 10:12:13|
|4|dog|2023-05-05 10:12:13|
|5|dog|2023-05-05 10:12:13|
|6|cat|2023-05-05 10:12:13|

We want to have resulted data like

|id|word|created_at|
|--|--|--|
|1|hello|2023-05-05 10:12:13|
|4|dog|2023-05-05 10:12:13|
|6|cat|2023-05-05 10:12:13|

## Solution

```SQL
DELETE FROM words WHERE id NOT in (
        SELECT MIN(id) FROM words GROUP BY word
    );
```

## Reference

- [https://stackoverflow.com/questions/51473852/sqlite3-deleting-rows-that-have-multiple-columns-of-the-same-value](https://stackoverflow.com/questions/51473852/sqlite3-deleting-rows-that-have-multiple-columns-of-the-same-value)