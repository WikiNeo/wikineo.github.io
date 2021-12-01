---
title: "[General] ENOSPC: System limit for number of file watchers reached"
published: true
tags: Linux
---

## Meaning

The meaning of this error is that the number of files monitored by the system
has reached the limit.

## Result

The command executed failed. Or throw a warning 

## Solution

Modify the number of system monitoring files

### Ubuntu

```
sudo gedit /etc/sysctl.conf
```

Add a line at the bottom

```
fs.inotify.max_user_watches=524288
```

Then save and exit

```
sudo sysctl -p
```

## Reference

- [React Native Error: ENOSPC: System limit for number of file watchers reached](https://stackoverflow.com/questions/55763428/react-native-error-enospc-system-limit-for-number-of-file-watchers-reached/56156015#56156015)