---
title: 'DBeaver Invalid Private Key'
published: true
tags: Linux
---

private key genereated by ssh-keygen starts with

```shell
-----BEGIN OPENSSH PRIVATE KEY-----
```

and not

```shell
-----BEGIN RSA PRIVATE KEY-----
```

and this is not supported by DBeaver.

To generated supported key add `-m PEM` to the end of your `ssh-keygen` command

e.g.

```shell
ssh-keygen -t rsa -b 2048 -m PEM
```

Run this on your key to convert it to RSA private key.

```shell
ssh-keygen -p -m PEM -f ~/.ssh/id_rsa
```