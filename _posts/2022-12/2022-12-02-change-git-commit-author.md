---
title: 'Change Git Commit User Name and Email'
published: true
tags: Git
---

```bash
git config --global user.name "New Author Name"
git config --global user.email "<email@address.example>"
```

## Single Commit

```shell
 git commit --amend --no-edit --reset-author
```

## Entire History

```shell
git rebase -r --root --exec "git commit --amend --no-edit --reset-author"
```

## Reference

- [https://stackoverflow.com/questions/750172/how-do-i-change-the-author-and-committer-name-email-for-multiple-commits](https://stackoverflow.com/questions/750172/how-do-i-change-the-author-and-committer-name-email-for-multiple-commits)