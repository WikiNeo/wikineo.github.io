---
title: 'Kernel modules'
published: true
tags: Linux
---

Kernel modules are object files that contain code to extend the kernel of an
operating system. Kernel modules are used to add support for new hardware
and/or filesystems, or for adding system calls. Modules can be built into the
kernel or compiled as loadable kernel modules.

Most modern Gentoo installations will use a device manager, such as `udev`, to
automatically load and manage kernel modules, thus module loading will often
need no particular configuration.

## About Loadable kernel modules

Many Loadable kernel modules (LKMs) may also be compiled "in-kernel". See configuring a kernel on how to select either built-in and LKM options.

Using LKMs can result in a smaller kernel memory footprint, by not having unneeded modules loaded: modules can be loaded on demand by udev (for example DVB drivers for a DVB stick). Compile-in-kernel code will not be able to be reloaded while the kernel is running, but LKMs can sometimes be used to solve certain issues, by unloading and reloading them.

Using a module rather than building code into the kernel also permits the
setting of module-specific parameters, through the `/etc/modprobe.d` file - see
`man /etc/modprobe.d`.

Modules needed early in the boot process may require an update of the initramfs after a kernel update or recompilation (e.g. filesystem drivers for filesystems used for boot). Some LKMs may incur a slight performance penalty over built-in code, due to the addition of an API layer and slightly more memory usage.

Beware of file system module X located on a partition formatted with X (unbootable system at worst).

## Reference

- [https://wiki.gentoo.org/wiki/Kernel_Modules](https://wiki.gentoo.org/wiki/Kernel_Modules)