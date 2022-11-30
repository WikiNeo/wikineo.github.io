---
title: 'Pacman Remove'
published: true
tags: ArchLinux
---

## OPERATION

```shell
-R, --remove
           Remove package(s) from the system. Groups can also be specified to be removed, in which
           case every package in that group will be removed. Files belonging to the specified package
           will be deleted, and the database will be updated. Most configuration files will be saved
           with a .pacsave extension unless the --nosave option is used. See Remove Options below.
```

## REMOVE OPTIONS (APPLY TO -R)

```shell
       -c, --cascade
           Remove all target packages, as well as all packages that depend on one or more target
           packages. This operation is recursive and must be used with care, since it can remove many
           potentially needed packages.

       -n, --nosave
           Instructs pacman to ignore file backup designations. Normally, when a file is removed from
           the system, the database is checked to see if the file should be renamed with a .pacsave
           extension.

       -s, --recursive
           Remove each target specified including all of their dependencies, provided that (A) they
           are not required by other packages; and (B) they were not explicitly installed by the
           user. This operation is recursive and analogous to a backwards --sync operation, and it
           helps keep a clean system without orphans. If you want to omit condition (B), pass this
           option twice.

       -u, --unneeded
           Removes targets that are not required by any other packages. This is mostly useful when
           removing a group without using the -c option, to avoid breaking any dependencies.
```