---
title: 'initramfs'
published: true
tags: Linux
---

An **initramfs** (**init**ial **ram** **f**ile **s**ystem) is used to prepare Linux systems during boot before the **init** process starts.

The initramfs usually takes care of mounting important file systems (by
loading the proper kernel modules and drivers) such as `/usr` or `/var`,
preparing the `/dev` file structure, etc. Users who use an encrypted file
system will also have the initramfs ask them for the passphrase before it can
mount the file systems. When the file systems are mounted, control is passed
on to **init** which then takes care of further starting all necessary services
and booting up the remainder of the system.

## Reference

- [https://wiki.gentoo.org/wiki/Initramfs](https://wiki.gentoo.org/wiki/Initramfs)
