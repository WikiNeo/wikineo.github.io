---
title: '[Gentoo] Custom ebuild repository'
published: true
tags: Linux
---

## Creating a local repository

```bash
sudo eselect repository create localrepo
```

## Adding an ebuild to the repository

```bash
sudo git clone git@github.com:mintwzy/localrepo.git
sudo chown -R portage:portage /var/db/repos/localrepo
sudo repoman manifest
```

## Install package

```bash
sudo emerge --ask --verbose dev-python/PyQt5
```

## Reference

- [https://wiki.gentoo.org/wiki/Custom_ebuild_repository](https://wiki.gentoo.org/wiki/Custom_ebuild_repository)