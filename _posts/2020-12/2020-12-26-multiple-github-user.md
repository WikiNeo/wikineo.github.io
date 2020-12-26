---
title: "Configure multiple Github user on the same PC"
published: true
tags: Git
---

Generate SSH key

```
ssh-keygen -t ed25519 -C "your_email@example.com"

OR

ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

```shell
~/.ssh/config

Host github.com
  HostName github.com
  User mintwzy
  IdentityFile ~/.ssh/id_rsa
Host github.com2
  HostName github.com
  User trusty-patches-mint
  IdentityFile ~/.ssh/id_ed25519

```

```shell
REPO/.git/config

[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
[remote "origin"]
        url = git@github.com2:trusty-patches-mint/trusty-patches-mint.github.io.git
        fetch = +refs/heads/*:refs/remotes/origin/*
```