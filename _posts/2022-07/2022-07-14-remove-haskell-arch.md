---
title: 'Remove Haskell Packages from Arch Linux'
published: true
tags: ArchLinux
---

```shell
pacman -Qq | grep haskell | sudo pacman -Rsn -
```

## DESCRIPTION

       Pacman is a package management utility that tracks installed packages on a Linux system. It features dependency
       support, package groups, install and uninstall scripts, and the ability to sync your local machine with a remote
       repository to automatically upgrade packages. Pacman packages are a zipped tar format.

       Since version 3.0.0, pacman has been the front-end to libalpm(3), the “Arch Linux Package Management” library. This
       library allows alternative front-ends to be written (for instance, a GUI front-end).

       Invoking pacman involves specifying an operation with any potential options and targets to operate on. A target is
       usually a package name, file name, URL, or a search string. Targets can be provided as command line arguments.
       Additionally, if stdin is not from a terminal and a single hyphen (-) is passed as an argument, targets will be read
       from stdin.


## OPERATIONS

	-Q, --query
           Query the package database. This operation allows you to view installed packages and their files, as well as
           meta-information about individual packages (dependencies, conflicts, install date, build date, size). This can be
           run against the local package database or can be used on individual package files. In the first case, if no package
           names are provided in the command line, all installed packages will be queried. Additionally, various filters can
           be applied on the package list. See Query Options below.

	-R, --remove
           Remove package(s) from the system. Groups can also be specified to be removed, in which case every package in that
           group will be removed. Files belonging to the specified package will be deleted, and the database will be updated.
           Most configuration files will be saved with a .pacsave extension unless the --nosave option is used. See Remove
           Options below.

### QUERY OPTIONS (APPLY TO -Q)

       -q, --quiet
           Show less information for certain query operations. This is useful when pacman’s output is processed in a script.
           Search will only show package names and not version, group, and description information; owns will only show
           package names instead of "file is owned by pkg" messages; group will only show package names and omit group names;
           list will only show files and omit package names; check will only show pairs of package names and missing files; a
           bare query will only show package names rather than names and versions.

### REMOVE OPTIONS (APPLY TO -R)

	-n, --nosave
           Instructs pacman to ignore file backup designations. Normally, when a file is removed from the system, the database
           is checked to see if the file should be renamed with a .pacsave extension.

       -s, --recursive
           Remove each target specified including all of their dependencies, provided that (A) they are not required by other
           packages; and (B) they were not explicitly installed by the user. This operation is recursive and analogous to a
           backwards --sync operation, and it helps keep a clean system without orphans. If you want to omit condition (B),
           pass this option twice.