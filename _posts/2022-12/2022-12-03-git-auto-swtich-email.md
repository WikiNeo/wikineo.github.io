---
title: 'Git Auto Switch Email'
published: true
tags: Git
---

```shell
$ cat ~/.gitconfig | head -5

[includeIf "gitdir:~/gh/**"]
    path = ~/.github.gitconfig

[includeIf "gitdir:~/work/**"]
    path = ~/.work.gitconfig

$ cat ~/.github.gitconfig

[user]
    name = MyName
    email = my-personal-emal@gmail.com

$ cat ~/.work.gitconfig

[user]
    name = MyName
    email = my-company-email@company.com
```

## Reference

- [https://stackoverflow.com/questions/56112638/how-to-auto-switch-email-address-by-url-in-git](https://stackoverflow.com/questions/56112638/how-to-auto-switch-email-address-by-url-in-git`)