---
title: '[SSH] ssh “permissions are too open” error'
published: true
tags: Linux
---

Keys need to be only readable by you:

```shell
chmod 400 ~/.ssh/id_rsa
```

If Keys need to be read-writable by you:

```shell
chmod 600 ~/.ssh/id_rsa
```

## Reference

- [https://stackoverflow.com/questions/9270734/ssh-permissions-are-too-open-error](https://stackoverflow.com/questions/9270734/ssh-permissions-are-too-open-error)