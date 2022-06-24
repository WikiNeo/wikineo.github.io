---
title: 'pyca/cryptography Mac install fails with fatal error: "openssl/opensslv.h" file not found'
published: true
tags: Python
---

When install `pyca/cryptography` on MacOS with python `2.7.18`, we got the
following error

```shell
build/temp.macosx-10.12-x86_64-2.7/_openssl.c:433:10: fatal error: 'openssl/opensslv.h' file not found
#include <openssl/opensslv.h>
```

## Solution

```shell
brew install openssl@1.1

pip install cryptography --global-option=build_ext --global-option="-L/usr/local/opt/openssl@1.1/lib" --global-option="-I/usr/local/opt/openssl@1.1/include"
```

## Reference

- [https://github.com/pyca/cryptography/issues/3489](https://github.com/pyca/cryptography/issues/3489)