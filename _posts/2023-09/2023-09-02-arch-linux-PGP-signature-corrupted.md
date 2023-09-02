---
title: "Arch Linux Pacman PGP Signatures are Corrupted"
published: true
tags: ArchLinux
---

Solve the issue with `sudo pacman -Syu` having `PGP Signatures are Corrupted`
error.

```shell
sudo pacman -Sy archlinux-keyring
```

## Reference

- [https://bbs.archlinux.org/viewtopic.php?id=278478](https://bbs.archlinux.org/viewtopic.php?id=278478)