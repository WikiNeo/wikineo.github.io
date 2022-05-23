---
title: 'Create MySQL user and grant permissions'
published: true
tags: MySQL
---

## All Permissions

```SQL
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost';
FLUSH PRIVILEGES;
```

## Read-only Permissions

```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT, SHOW VIEW ON *.* TO 'newuser'@'localhost';
FLUSH PRIVILEGES;
```

## Reference

- [https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)