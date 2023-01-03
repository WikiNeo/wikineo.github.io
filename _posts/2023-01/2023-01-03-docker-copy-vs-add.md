---
title: "Docker COPY vs ADD"
published: true
tags: Docker
---

```go
// ADD foo /path
//
// Add the file 'foo' to '/path'. Tarball and Remote URL (http, https) handling
// exist here. If you do not wish to have this automatic handling, use COPY.


// COPY foo /path
//
// Same as 'ADD' but without the tar and remote url handling.
```

## Reference

- [https://github.com/moby/moby/blob/22.06/builder/dockerfile/dispatchers.go#L86](https://github.com/moby/moby/blob/22.06/builder/dockerfile/dispatchers.go#L86)
- [https://github.com/moby/moby/blob/22.06/builder/dockerfile/dispatchers.go#L110](https://github.com/moby/moby/blob/22.06/builder/dockerfile/dispatchers.go#L110)