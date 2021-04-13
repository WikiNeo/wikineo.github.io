---
title: 'Fix "_mysql.c:44:10: fatal error: 'my_config.h' file not found" when
installing mysql-python on MacOS'
published: true
tags: MacOS
---

```shell
brew remove mysql
brew install mysql@5.7
brew link --force mysql@5.7
pip install mysql-python
```

## Reference

- [https://stackoverflow.com/questions/50864438/mac-pip-install-mysql-python-unsuccessful](https://stackoverflow.com/questions/50864438/mac-pip-install-mysql-python-unsuccessful)