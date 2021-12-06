---
title: '[Gentoo] Ignore file collision on emerge'
published: true
tags: Gentoo
---

Add `FEATURES`

```bash
FEATURES="-collision-detect -protect-owned" emerge =sys-devel/gcc-4.2.4
```

## Reference

- [https://forums.gentoo.org/viewtopic-t-718149.html](https://forums.gentoo.org/viewtopic-t-718149.html)

