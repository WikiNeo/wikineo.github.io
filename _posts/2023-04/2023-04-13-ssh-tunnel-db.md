---
title: "Connect Remote MySQL Database Through SSH Tunneling"
published: true
tags: MySQL
---

## Start SSH Tunnel

```shell
ssh -N -L 3307:$DB_URL -i /path/to/pem user@base -oHostKeyAlgorithms=+ssh-rsa -o 'PubkeyAcceptedKeyTypes +ssh-rsa'
```

## Connect from local machine

```shell
mysql -u remote_db_user -h 127.0.0.1 -P 3307 -p
```
