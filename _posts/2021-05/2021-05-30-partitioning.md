---
title: 'Partitioning'
published: true
tags: FileSystem
---

From Wikipedia:

    Disk partitioning or disk slicing is the creation of one or more regions on secondary storage, so that each region can be managed separately.

An entire disk may be allocated to a single partition, or multiple ones for cases such as dual-booting, maintaining a swap partition, or to logically separate data such as audio and video files. The partitioning scheme is stored in a partition table such as Master Boot Record (MBR) or GUID Partition Table (GPT).

Partition tables are created and modified using one of many partitioning tools. The tools available for Arch Linux are listed in the #Partitioning tools section.

Partitions usually contain a file system directly which is accomplished by creating a file system on (a.k.a. formatting) the partition. Alternatively, partitions can contain LVM, block device encryption or RAID, which ultimately provide device files on which a file system can be placed (or the devices can be stacked further).

Any block device (e.g. disk, partition, LUKS device, LVM logical volume or RAID array) that directly contains a mountable file system is called a volume.

## Reference

- [https://wiki.archlinux.org/title/Partitioning](https://wiki.archlinux.org/title/Partitioning)