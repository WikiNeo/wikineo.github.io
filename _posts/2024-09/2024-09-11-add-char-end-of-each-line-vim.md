---
title: Neovim add a string to the end of each line
published: true
tags: Neovim
---

```vimscript
:%norm A*
```

Explanation

```vimscript
 %       = for every line
 norm    = type the following commands
 A*      = append '*' to the end of current line
```

## Reference

- [https://stackoverflow.com/questions/594448/how-can-i-add-a-string-to-the-end-of-each-line-in-vim](https://stackoverflow.com/questions/594448/how-can-i-add-a-string-to-the-end-of-each-line-in-vim)
