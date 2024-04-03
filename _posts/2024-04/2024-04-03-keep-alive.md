---
title: "Keep-Alive"
published: true
tags: Network
---

The Keep-Alive general header allows the sender to hint about how the connection may be used to set a timeout and a
maximum amount of requests.

## Syntax

```HTTP
Keep-Alive: parameters
```

## Directives

### parameters

A comma-separated list of parameters, each consisting of an identifier and a value separated by the equal sign (`'='`).
The following identifiers are possible:

- `timeout`: An integer that is the time in seconds that the host will allow an idle connection to remain open before
  it is closed. A connection is idle if no data is sent or received by a host. A host may keep an idle connection open
  for longer than `timeout` seconds, but the host should attempt to retain a connection for at least `timeout` seconds.
- `max`: An integer that is the maximum number of requests that can be sent on this connection before closing it.
  Unless `0`, this value is ignored for non-pipelined connections as another request will be sent in the next response.
  An HTTP pipeline can use it to limit the pipelining.

## Examples

A response containing a `Keep-Alive` header

```HTTP
HTTP/1.1 200 OK
Connection: Keep-Alive
Content-Encoding: gzip
Content-Type: text/html; charset=utf-8
Date: Thu, 11 Aug 2016 15:23:13 GMT
Keep-Alive: timeout=5, max=1000
Last-Modified: Mon, 25 Jul 2016 04:32:39 GMT
Server: Apache

(body)
```
