---
title: "How to get the total size of a directory from the command line"
published: true
tags: Ubuntu
---

The command `du` "Summarizes disk usage of each FILE, recursively for
directories," e.g.,

```bash
du -hs /path/to/directory
```

- `-h` is to get the numbers "human readable", e.g. get `140M` instead of
  `143260` (size in KButes)
- `-s` is for summary (otherwise you'll et not only the size of the folder but
  also for everything in the folder separately)

-----------------------------------------------

As you're using `-h` you can sort the human readable values using

```bash
du -h | sort -h
```

The `-h` flag on `sort` will consider "Human Readable" size values.

-------------------------------------------------

If you want to avoid recursively listing all files and directories, you can
supply the `--max-depth` parameter to limit how many items are displayed. Most
commonly, `--max-depth=1`

```bash
du -h --max-depth=1 /path/to/directory
```

## References

- [https://askubuntu.com/questions/1224/how-do-i-determine-the-total-size-of-a-directory-folder-from-the-command-line](https://askubuntu.com/questions/1224/how-do-i-determine-the-total-size-of-a-directory-folder-from-the-command-line)