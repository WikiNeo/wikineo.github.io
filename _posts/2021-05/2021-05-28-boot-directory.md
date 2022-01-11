---
title: 'The /boot directory'
published: true
tags: FileSystem
---

This directory contains everything required for the boot process except for configuration files not needed at boot time (the most notable of those being those that belong to the GRUB boot-loader) and the map installer. Thus, the /boot directory stores data that is used before the kernel begins executing user-mode programs. This may include redundant (back-up) master boot records, sector/system map files, the kernel and other important boot files and data that is not directly edited by hand. Programs necessary to arrange for the boot loader to be able to boot a file are placed in /sbin. Configuration files for boot loaders are placed in /etc. The system kernel is located in either / or /boot (or as under Debian in /boot but is actually a symbolically linked at / in accordance with the FSSTND).

## Reference

- [https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/boot.html](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/boot.html)