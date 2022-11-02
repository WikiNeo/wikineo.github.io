---
title: 'HTTP Host Headers'
published: true
tags: Network
---

The `Host` request header specifies the host and port number of the server to
which the request is being sent.

If no port is included, the default port for the service requested is implied
(e.g., `443` for an HTTPS URL, and `80` for an HTTP URL).

A `Host` header field must be sent in all HTTP/1.1 request messages. A 400 (Bad
Request) status code may be sent to any HTTP/1.1 request message that lacks or
contains more than one `Host` header field.

## Syntax

```
Host: <host>:<port>
```

## Directives

- `<host>`
  - the domain name of the server (for virtual hosting).
- `<port>`
  - TCP port number on which the server is listening.

## Examples

```
Host: developer.mozilla.org
```

## Reference

- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host)