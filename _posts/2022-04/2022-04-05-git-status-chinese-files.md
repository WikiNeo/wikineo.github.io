---
title: 'Solve the problem of garbled Chinese file name in Git status display'
published: true
tags: Git
---

When using git status to view the changed but uncommitted Chinese file name, it is found that it will be displayed as a string of numbers, and the Chinese file name is not displayed. The details are as follows:

```
$ git status
#In branch master
#Changes that have not been staged for submission:
#(use "git add < File >..." to update the content to be submitted)
#(use "git checkout -- < File >..." to discard changes to the workspace)
#
#Modification: "224 / 257 / 346 / 216 / 247 / 345 / 210 / 266 / 346 / 265 / 201. TXT"
```

The solution is to set `core.quotepath` option is false:

```
git config --global core.quotepath false
```

## core.quotePath

> Commands that output paths (e.g. ls-files, diff), will quote “unusual” characters in the pathname by enclosing the pathname in double-quotes and escaping those characters with backslashes in the same way C escapes control characters (e.g. t for TAB, n for LF, \ for backslash) or bytes with values larger than 0x80 (e.g. octal 302265 for “micro” in UTF-8). If this variable is set to false, bytes higher than 0x80 are not considered “unusual” any more. Double-quotes, backslash and control characters are always escaped regardless of the setting of this variable. A simple space character is not considered “unusual”. Many commands can output pathnames completely verbatim using the -z option. The default value is true.

## Reference

- [https://developpaper.com/solve-the-problem-of-garbled-chinese-file-name-in-git-status-display/](https://developpaper.com/solve-the-problem-of-garbled-chinese-file-name-in-git-status-display/)