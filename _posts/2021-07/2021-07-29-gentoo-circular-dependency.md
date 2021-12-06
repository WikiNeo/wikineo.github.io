---
title: '[Gentoo] Solve Circular Dependency for harfbuzz & freetype'
published: true
tags: Gentoo
---

Error log

```shell
Total: 3 packages (3 reinstalls), Size of downloads: 0 KiB

 * Error: circular dependencies:

(media-libs/harfbuzz-2.8.1:0/0.9.18::gentoo, ebuild scheduled for merge) depends on
 (media-libs/freetype-2.10.4:2/2::gentoo, ebuild scheduled for merge) (buildtime_slot_op)
  (media-libs/harfbuzz-2.8.1:0/0.9.18::gentoo, ebuild scheduled for merge) (buildtime)

 * Note that circular dependencies can often be avoided by temporarily
 * disabling USE flags that trigger optional dependencies.
```

Directly remove `harfbuzz` USE flag for `freetype` doesn't work.

```shell
       --oneshot, -1
              Emerge as normal, but do not add the packages to the world file for later updating.

              WARNING:  This option should only be used for packages that are reachable from the @world package set (those that would not be removed by --depclean), since dependencies of unreachable packages are allowed to be broken when satisfying dependencies of other packages.  Broken dependencies of this sort will invalidate assumptions that make it possible for
              --deep to be disabled by default.
       --nodeps, -O
              Merges specified packages without merging any dependencies.  Note that the build may fail if the dependencies aren't satisfied.
```

So let's install the dependencies manually and then reinstall `harfbuzz` &
`freetype`

```shell
# USE="-harfbuzz" emerge -1 virtual/libintl app-arch/bzip2 virtual/libiconv media-libs/libpng dev-libs/libpcre media-libs/freetype media-gfx/graphite2 sys-apps/util-linux dev-libs/glib media-libs/harfbuzz --nodeps
# emerge -1 media-libs/freetype media-libs/harfbuzz
```

## Reference

- [https://forums.gentoo.org/viewtopic-p-8632444.html?sid=c7fa8cff642a2435e1dfbce7d9cef6ec][https://forums.gentoo.org/viewtopic-p-8632444.html?sid=c7fa8cff642a2435e1dfbce7d9cef6ec]