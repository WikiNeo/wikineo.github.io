---
title: 'The /run directory'
published: true
tags: Linux
---

Apparently, many tools (among them udev) will soon require a /run/ directory that is mounted early (as tmpfs). Arch developers introduced /run last month to prepare for this.

The udev runtime data moved from /dev/.udev/ to /run/udev/. The /run mountpoint is supposed to be a tmpfs mounted during early boot, available and writable to for all tools at any time during bootup, it replaces /var/run/, which should become a symlink some day. 

## Reference

- [https://unix.stackexchange.com/questions/13972/what-is-this-new-run-filesystem](https://unix.stackexchange.com/questions/13972/what-is-this-new-run-filesystem)