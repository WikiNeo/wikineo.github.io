---
title: 'EFI system partition'
published: true
tags: FileSystem
---

The EFI system partition (also called ESP) is an OS independent partition that acts as the storage place for the EFI bootloaders, applications and drivers to be launched by the UEFI firmware. It is mandatory for UEFI boot.

The UEFI specification mandates support for the FAT12, FAT16, and FAT32 file systems (see UEFI specification version 2.8, section 13.3.1.1), but any conformant vendor can optionally add support for additional file systems; for example, the firmware in Apple Macs supports the HFS+ file system.

## Reference

- [https://wiki.archlinux.org/title/EFI_system_partition](https://wiki.archlinux.org/title/EFI_system_partition)