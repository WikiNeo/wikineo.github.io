---
title: 'Copy MySQL data folder'
published: true
tags: MySQL
---

I often install different Linux OS, to save the time for MySQL setup, do the following.

```shell
sudo cp -R mysql-data-folder /var/lib/mysql
sudo chown -R mysql:mysql /var/lib/mysql
```