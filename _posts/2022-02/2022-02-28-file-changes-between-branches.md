---
title: 'Git Show File Changes Between Branches'
published: true
tags: Git
---

## Compare current branch against main branch

```
git diff --name-status main
```

## Compare any two branches

``
git diff --name-status firstbranch..yourBranchName
```

## Reference

- [https://stackoverflow.com/questions/822811/showing-which-files-have-changed-between-two-revisions](https://stackoverflow.com/questions/822811/showing-which-files-have-changed-between-two-revisions)