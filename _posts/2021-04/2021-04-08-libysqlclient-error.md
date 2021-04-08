---
title: 'Fix "libmysqlclient.so.20: cannot open shared object file: No such file or directory"'
published: true
tags: Ruby
---

This error can be caused by the `mysql2` gem under mysterious circumstances. You
need to remove it with `gem uninstall mysql2` and then reinstall it (or just run
bundle).

`gem pristine mysql2` will not be enough.

## Reference

- [https://makandracards.com/makandra/42502-fix-libmysqlclient-so-20-cannot-open-shared-object-file-no-such-file-or-directory](https://makandracards.com/makandra/42502-fix-libmysqlclient-so-20-cannot-open-shared-object-file-no-such-file-or-directory)