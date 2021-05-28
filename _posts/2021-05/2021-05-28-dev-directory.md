---
title: 'The /dev directory'
published: true
tags: Linux
---

The /dev directory contains the special device files for all the devices. The
device files are created during installation, and later with the /dev/MAKEDEV
script. The /dev/MAKEDEV.local is a script written by the system administrator
that creates local-only device files or links (i.e. those that are not part of
the standard MAKEDEV, such as device files for some non-standard device driver).

## Samples

- **/dev/null**

    The bit bucket. A black hole where you can send data for it never to be seen again. Anything sent to /dev/null will disappear. This can be useful if, for example, you wish to run a command but not have any feedback appear on the terminal. It is a character device on major node 1 and minor node 3.

## Reference

- [https://tldp.org/LDP/sag/html/dev-fs.html](https://tldp.org/LDP/sag/html/dev-fs.html)