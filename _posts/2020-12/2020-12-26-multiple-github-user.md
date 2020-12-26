---
title: "Configure multiple Github user on the same PC"
published: true
tags: Git
---

## Generate SSH key

```
ssh-keygen -t ed25519 -C "your_email@example.com"

OR

ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

## Add SSH key to Github

```
Settings/SSH and GPG keys
```

## .ssh/config

```shell
Host github.com
  HostName github.com
  User mintwzy
  IdentityFile ~/.ssh/id_rsa
Host github.com2
  HostName github.com
  User trusty-patches-mint
  IdentityFile ~/.ssh/id_ed25519
```

## REPO/.git/config

```shell
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
[remote "origin"]
        url = git@github.com2:trusty-patches-mint/trusty-patches-mint.github.io.git
        fetch = +refs/heads/*:refs/remotes/origin/*
```