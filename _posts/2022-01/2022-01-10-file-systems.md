---
title: '[Arch Wiki] File Systems'
published: true
tags: FileSystem
---

From Wikipedia:

	In computing, a file system or filesystem controls how data is stored and
	retrieved. Without a file system, information placed in a storage medium would
	be one large body of data with no way to tell where one piece of information
	stops and the next begins. By separating the data into pieces and giving each
	piece a name, the information is easily isolated and identified. Taking its name
	from the way paper-based information systems are named, each group of data is
	called a "file". The structure and logic rules used to manage the groups of
	information and their names is called a "file system".

## Identify existing file systems

```shell
$ lsblk -f
NAME   FSTYPE LABEL     UUID                                 MOUNTPOINT
sdb                                                          
└─sdb1 vfat   Transcend 4A3C-A9E9
```

## Mount a file system

To manually mount a file system located on a device (e.g., a partition) to a directory, use mount(8). This example mounts `/dev/sda1` to `/mnt`.

```
# mount /dev/sda1 /mnt
```

This attaches the file system on `/dev/sda1` at the directory `/mnt`, making the
contents of the file system visible. Any data that existed at `/mnt` before this
action is made invisible until the device is unmounted.

fstab contains information on how devices should be automatically mounted if
present. See the fstab article for more information on how to modify this
behavior.

## List mounted file systems

To list all mounted file systems, use findmnt(8):

```
$ findmnt
```

## Unmount a file system

To unmount a file system use umount(8). Either the device containing the file system (e.g., /dev/sda1) or the mount point (e.g., /mnt) can be specified:

```
# umount /dev/sda1
```

or

```
# umount /mnt
```

## Reference

- [https://wiki.archlinux.org/title/File_systems#Mount_a_file_system](https://wiki.archlinux.org/title/File_systems#Mount_a_file_system)