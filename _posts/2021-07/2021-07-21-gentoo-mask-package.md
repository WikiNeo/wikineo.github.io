---
title: '[Gentoo] Mask Package & Downgrade'
published: true
tags: Linux
---

## Problem

The `dev-python/PyQt5-5.15.4-r1` drops `webkit` use flag, which is required for
`ldoce5viewer`.

## Solution

Mask `dev-python/PyQt5` versions larger than `5.12.2` in `/etc/portage/package.mask`

```shell
>dev-python/PyQt5-5.12.2
```

Update the `world`

```shell
sudo emerge -DuNpv world
```

## man emerge

```shell
--deep [DEPTH], -D
       This flag forces emerge to consider the entire dependency tree of packages, instead of checking only the immedi‐
       ate dependencies of the packages.  As an example, this catches updates in libraries that are not directly listed
       in the dependencies of a package.  Also see --with-bdeps for behavior with respect to  build  time  dependencies
       that are not strictly required.
       
--update, -u
       Updates packages to the best version available, which may not always be the highest version number due to  mask‐
       ing for testing and development. Package atoms specified on the command line are greedy, meaning that unspecific
       atoms may match multiple versions of slotted packages.  This option also implies the --selective option.

--newuse, -N
       Tells emerge to include installed packages where USE flags have changed since compilation. This option also  im‐
       plies the --selective option.  USE flag changes include:

       A USE flag was added to a package.  A USE flag was removed from a package.  A USE flag was turned on for a pack‐
       age.  A USE flag was turned off for a package.

       USE flags may be toggled by your profile as well as your USE and package.use settings. If you would like to skip
       rebuilds for which disabled flags have been added to or removed from IUSE, see the related --changed-use option.
       If you would like to skip rebuilds for specific packages, see the --exclude option.

       NOTE: This option ignores the state of the "test" USE flag, since that  flag  has  a  special  binding  to  FEA‐
       TURES="test" (see make.conf(5) for more information about FEATURES settings).
       
--pretend, -p
       Instead of actually performing the merge, simply display what *would* have been installed if  --pretend  were not
       used.  Using --pretend is strongly recommended before installing an unfamiliar package.  In the printout:

       N   new (not yet installed)
       S   new SLOT installation (side-by-side versions)
       U   updating (to another version)
       D   downgrading (best version seems lower)
       r   reinstall (forced for some reason, possibly due to slot or sub-slot)
       R   replacing (remerging same version)
       F   fetch restricted (must be manually downloaded)
       f   fetch restricted (already downloaded)
       I   interactive (requires user input)
       B   blocked by another package (unresolved conflict)
       b   blocked by another package (automatically resolved conflict)

--verbose [ y | n ], -v
       Tell emerge to run in verbose mode.  Currently this flag causes emerge to print out GNU info errors, if any, and
       to show the USE flags that will be used for each package when pretending. The following symbols are  affixed  to
       USE flags in order to indicate their status:

       Symbol   Location    Meaning
       ──────────────────────────────────────────────────────────────

       -        prefix      not enabled (either disabled or removed)
       *        suffix      transition to or from the enabled state
       %        suffix      newly added or removed
       ()       circumfix   forced, masked, or removed
       {}       circumfix   state is bound to FEATURES settings
```

## Reference

- [https://forums.gentoo.org/viewtopic-p-6952644.html](https://forums.gentoo.org/viewtopic-p-6952644.html)
- [https://packages.gentoo.org/packages/dev-python/PyQt5](https://packages.gentoo.org/packages/dev-python/PyQt5)