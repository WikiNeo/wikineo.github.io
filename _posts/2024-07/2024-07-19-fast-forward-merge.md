---
title: Fast forward merge
published: true
tags: Git
---

A fast-forward merge can occur when there is a linear path from the current
branch tip to the target branch. Instead of “actually” merging the branches, all
Git has to do to integrate the histories is move (i.e., “fast forward”) the
current branch tip up to the target branch tip. This effectively combines the
histories, since all of the commits reachable from the target branch are now
available through the current one.

When you try to merge one commit with a commit that can be reached by following
the first commit’s history, Git simplifies things by moving the pointer forward,
because there isn't any divergent work to merge together—this is called a
fast-forward.

## Reference

- [https://www.atlassian.com/git/tutorials/using-branches/git-merge](https://www.atlassian.com/git/tutorials/using-branches/git-merge)
- [https://stackoverflow.com/questions/29673869/what-is-git-fast-forwarding](https://stackoverflow.com/questions/29673869/what-is-git-fast-forwarding)
