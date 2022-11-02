---
title: 'HTTP Connection Headers'
published: true
tags: Network
---

The `Connection` general header controls whether the network connection stays
open after the current transaction finishes. If the value sent is `keep-alive`,
the connection is persistent and not closed, allowing for subsequent requests
to the same server to be done.

## Syntax

```
Connection: keep-alive
Connection: close
```

## Directives

- `close`
  - Indicates that either the client or the server would like to close the connection. This is the default on HTTP/1.0 requests.

- any comma-separated list of HTTP headers [Usually `keep-alive` only]
  - Indicates that the client would like to keep the connection open. Keeping a connection open is the default on HTTP/1.1 requests. The list of headers are the name of the header to be removed by the first non-transparent proxy or cache in-between: these headers define the connection between the emitter and the first entity, not the destination node.

## Reference

- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Connection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Connection)