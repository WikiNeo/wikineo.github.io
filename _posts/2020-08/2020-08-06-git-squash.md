---
title: "Git Squash"
published: true
tags: Git
---

## Squash recent 3 commits into a single commit

```Bash
git rebase -i HEAD~3
```

change

```git
pick fda59df commit 1
pick x536897 commit 2
pick c01a668 commit 3
```

to

```git
pick fda59df commit 1
squash x536897 commit 2
squash c01a668 commit 3
```