---
title: "Change MySQL max_allowed_packet"
published: true
tags: MySQL 
---

## Find MySQL configuration files

```
mysqld --verbose --help | less
```

## Change max_allowed_packet

Under `[mysqld]` or `[client]` section change

```
max_allowed_packet=500M
```

then restart MySQL service.

## Reference

- [https://stackoverflow.com/questions/580331/determine-which-mysql-configuration-file-is-being-used](https://stackoverflow.com/questions/580331/determine-which-mysql-configuration-file-is-being-used)
- [https://stackoverflow.com/questions/8062496/how-to-change-max-allowed-packet-size](https://stackoverflow.com/questions/8062496/how-to-change-max-allowed-packet-size)