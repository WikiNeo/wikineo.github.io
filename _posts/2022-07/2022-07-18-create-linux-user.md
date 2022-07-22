---
title: 'Create a Linux user'
published: true
tags: Linux
---

The groups the user is member of define what activities the user can perform.

For instance, to create a user called larry who is member of the *wheel*, *users*,
and *audio* groups, log in as root first (only root can create users) and run
**useradd**:

```shell
Login: root
Password: (Enter the root password)

root # useradd -m -G users,wheel,audio -s /bin/bash larry
root # passwd larry
Password: (Enter the password for larry)
Re-enter password: (Re-enter the password to verify)
```

## Reference

- [https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Finalizing](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Finalizing)