---
title: "Vim Insert at the Beginning/End of Lines"
published: true
tags: Neovim
---

## Beginning

- Press `Esc` to enter `command mode`
- Use `Ctrl` + `v` to enter visual block mode
- Move `Up`/`Down` to select the columns of text in the lines you want to
  comment
- Then hit `Shift` + `i` and type the text you want to insert.
- Then hit `Esc`

## End

Insert `*` at the end of each line.

`:%s/$/\*/g`

## References

- [https://stackoverflow.com/questions/253380/how-to-insert-text-at-beginning-of-a-multi-line-selection-in-vi-vim](https://stackoverflow.com/questions/253380/how-to-insert-text-at-beginning-of-a-multi-line-selection-in-vi-vim)
- [https://stackoverflow.com/questions/594448/how-can-i-add-a-string-to-the-end-of-each-line-in-vim](https://stackoverflow.com/questions/594448/how-can-i-add-a-string-to-the-end-of-each-line-in-vim)